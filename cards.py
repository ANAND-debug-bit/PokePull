# inserting images from pokemondb.net for card art, since the official site doesn't have a good way to link to images directly. the (large) version is 512x512, which is a good size for my project.

def art(name):
    return "https://img.pokemondb.net/artwork/large/" + name + ".jpg"


TIERS = {
    "common":   {"points": 1,  "weight": 40, "label": "Common"},
    "uncommon": {"points": 2,  "weight": 27, "label": "Uncommon"},
    "rare":     {"points": 4,  "weight": 18, "label": "Rare"},
    "ultra":    {"points": 7,  "weight": 11, "label": "Ultra Rare"},
    "secret":   {"points": 15, "weight": 4,  "label": "Secret"},
}

BLURBS = {
    "common": [
        "{name} shows up on basically every other pull, you'll get used to seeing it.",
        "nothing fancy about {name}, it's the bread and butter of this pool.",
        "{name} again, the odds aren't exactly hiding how common this one is.",
    ],
    "uncommon": [
        "{name} isn't rare but it's a step up from filler, decent pull.",
        "people are happy enough to see {name} land in their hand.",
        "{name} sits comfortably in the middle of the pack.",
    ],
    "rare": [
        "{name} doesn't turn up every match, worth a small celebration.",
        "a {name} pull usually shifts the scoreboard a bit.",
        "{name} is the kind of card that gets a reaction across the table.",
    ],
    "ultra": [
        "{name} is a genuinely strong pull, this doesn't happen often.",
        "the odds were stacked against {name} showing up, and it still did.",
        "{name} landing here could swing the whole match.",
    ],
    "secret": [
        "{name}, the rarest tier in the pool, barely a few percent chance.",
        "{name} pulling here is the kind of moment people remember.",
        "almost nobody walks away from a match having pulled {name}.",
    ],
}

# tried to keep these roughly grouped by tier, easier to eyeball counts that way
CARDS = [
    # common
    {"name": "Caterpie",   "tier": "common", "img": art("caterpie")},
    {"name": "Weedle",     "tier": "common", "img": art("weedle")},
    {"name": "Rattata",    "tier": "common", "img": art("rattata")},
    {"name": "Pidgey",     "tier": "common", "img": art("pidgey")},
    {"name": "Zubat",      "tier": "common", "img": art("zubat")},
    {"name": "Magikarp",   "tier": "common", "img": art("magikarp")},
    {"name": "Bidoof",     "tier": "common", "img": art("bidoof")},
    {"name": "Sentret",    "tier": "common", "img": art("sentret")},
    {"name": "Poochyena",  "tier": "common", "img": art("poochyena")},
    {"name": "Wurmple",    "tier": "common", "img": art("wurmple")},
    {"name": "Hoothoot",   "tier": "common", "img": art("hoothoot")},
    {"name": "Spearow",    "tier": "common", "img": art("spearow")},
    {"name": "Ekans",      "tier": "common", "img": art("ekans")},
    {"name": "Ledyba",     "tier": "common", "img": art("ledyba")},
    {"name": "Hoppip",     "tier": "common", "img": art("hoppip")},

    # uncommon
    {"name": "Pikachu",    "tier": "uncommon", "img": art("pikachu")},
    {"name": "Eevee",      "tier": "uncommon", "img": art("eevee")},
    {"name": "Growlithe",  "tier": "uncommon", "img": art("growlithe")},
    {"name": "Vulpix",     "tier": "uncommon", "img": art("vulpix")},
    {"name": "Machop",     "tier": "uncommon", "img": art("machop")},
    {"name": "Abra",       "tier": "uncommon", "img": art("abra")},
    {"name": "Squirtle",   "tier": "uncommon", "img": art("squirtle")},
    {"name": "Charmander", "tier": "uncommon", "img": art("charmander")},
    {"name": "Bulbasaur",  "tier": "uncommon", "img": art("bulbasaur")},
    {"name": "Psyduck",    "tier": "uncommon", "img": art("psyduck")},
    {"name": "Meowth",     "tier": "uncommon", "img": art("meowth")},
    {"name": "Bellsprout", "tier": "uncommon", "img": art("bellsprout")},

    # rare
    {"name": "Charmeleon", "tier": "rare", "img": art("charmeleon")},
    {"name": "Wartortle",  "tier": "rare", "img": art("wartortle")},
    {"name": "Ivysaur",    "tier": "rare", "img": art("ivysaur")},
    {"name": "Gengar",     "tier": "rare", "img": art("gengar")},
    {"name": "Alakazam",   "tier": "rare", "img": art("alakazam")},
    {"name": "Machamp",    "tier": "rare", "img": art("machamp")},
    {"name": "Snorlax",    "tier": "rare", "img": art("snorlax")},
    {"name": "Lapras",     "tier": "rare", "img": art("lapras")},
    {"name": "Scyther",    "tier": "rare", "img": art("scyther")},
    {"name": "Gyarados",   "tier": "rare", "img": art("gyarados")},

    # ultra rare
    {"name": "Charizard",  "tier": "ultra", "img": art("charizard")},
    {"name": "Blastoise",  "tier": "ultra", "img": art("blastoise")},
    {"name": "Venusaur",   "tier": "ultra", "img": art("venusaur")},
    {"name": "Tyranitar",  "tier": "ultra", "img": art("tyranitar")},
    {"name": "Garchomp",   "tier": "ultra", "img": art("garchomp")},
    {"name": "Lucario",    "tier": "ultra", "img": art("lucario")},
    {"name": "Greninja",   "tier": "ultra", "img": art("greninja")},
    {"name": "Umbreon",    "tier": "ultra", "img": art("umbreon")},

    # secret - keep this pool small on purpose
    {"name": "Mewtwo",     "tier": "secret", "img": art("mewtwo")},
    {"name": "Mew",        "tier": "secret", "img": art("mew")},
    {"name": "Rayquaza",   "tier": "secret", "img": art("rayquaza")},
    {"name": "Arceus",     "tier": "secret", "img": art("arceus")},
    {"name": "Lugia",      "tier": "secret", "img": art("lugia")},
]