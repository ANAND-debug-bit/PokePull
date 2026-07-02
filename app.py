import random
from flask import Flask, render_template, request, redirect, url_for, session

from cards import CARDS, TIERS, BLURBS

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="/static")
app.secret_key = "poke-pull-dev-key-change-this-if-you-deploy"  

TOTAL_ROUNDS = 3

def fresh_state():
    return {
        "round": 1,
        "turn": 0,  
        "game_over": False,
        "p1_name": "Player 1",
        "p2_name": "Player 2",
        "p1_score": 0,
        "p2_score": 0,
        "p1_rolls": [],
        "p2_rolls": [],
        "last_card": None,}

def get_state():
    if "game" not in session:
        session["game"] = fresh_state()
    return session["game"]

def save_state(state):
    session["game"] = state

# picking a rarity tier randomly but weighted, so rare stuff shows up way less
def pick_tier():
    roll = random.uniform(0, 100)
    acc = 0
    for key, info in TIERS.items():
        acc += info["weight"]
        if roll <= acc:
            return key
    return "common"  # just in case the math doesn't add up to exactly 100, fallback


# once we know the tier, it will grab  a random card that belongs to that tier 
def pick_card(tier):
    pool = [c for c in CARDS if c["tier"] == tier]
    return random.choice(pool)

def pick_blurb(tier, name):
    line = random.choice(BLURBS[tier])
    return line.replace("{name}", name)

@app.route("/")
def home():
    state = get_state()
    return render_template(
        "index.html",
        state=state,
        tiers=TIERS,
        total_rounds=TOTAL_ROUNDS,
    )

# when the player click on the roll button
@app.route("/roll", methods=["POST"])
def roll():
    state = get_state()
    if state["game_over"]:
        return redirect(url_for("home"))  

    tier = pick_tier()
    card = pick_card(tier)
    points = TIERS[tier]["points"]
    blurb = pick_blurb(tier, card["name"])

    roll_entry = {
        "name": card["name"],
        "tier": tier,
        "label": TIERS[tier]["label"],
        "points": points,
        "img": card["img"],
        "blurb": blurb,
    }

    if state["turn"] == 0:
        state["p1_score"] += points
        state["p1_rolls"].insert(0, roll_entry)  
    else:
        state["p2_score"] += points
        state["p2_rolls"].insert(0, roll_entry)

    state["last_card"] = roll_entry

    state["turn"] = 1 - state["turn"]

    if state["turn"] == 0:
        state["round"] += 1

    if state["round"] > TOTAL_ROUNDS:
        state["game_over"] = True

    save_state(state)
    return redirect(url_for("home"))


#adding their own name to the game makes it more interesting to play
@app.route("/names", methods=["POST"])
def set_names():
    state = get_state()
    p1 = request.form.get("p1_name", "").strip()
    p2 = request.form.get("p2_name", "").strip()
    state["p1_name"] = p1 or "Player 1"
    state["p2_name"] = p2 or "Player 2"
    save_state(state)
    return redirect(url_for("home"))

@app.route("/reset", methods=["POST"])
def reset():
    session["game"] = fresh_state()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)

