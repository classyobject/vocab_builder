"""
    Copyright (c) 2021 SS
    File name: wordlist.py
    Author: SS
    Date created: 2021-3-28
    Date last modified: 2021-3-28
    Python Version: 3.8
"""


import copy


class WordList:
    _all = []   # Silently concatenate all list instances
    def __init__(self, words, category=''):
        self.words = copy.deepcopy(words)
        self.category = category
        WordList._all.append(self.words)


# Library of word lists organized as categories
# Use _ (underscore) to denote antonym

EMOTIONS = [
"acceptance", "admiration", "affection", "aggravation", "anger", "anguish", "anxiety", "attraction", "boredom", "caution", "certainty", "compassion", "confidence", "confusion", "contentment", "courage", "curiosity", "defeat", "defiance", "delight", "dependence", "depression", "desire", "disappointment", "dislike", "dismay", "distress", "embarrassment", "enthusiasm", "envy", "excitement", "fear", "frustration", "fury", "generosity", "greed", "grief", "guilt", "hate", "hatred", "hope", "horror", "hostility", "impatience", "jealousy", "joy", "kindness", "loneliness", "longing", "love", "lust", "malice", "misery", "optimism", "panic", "patience", "pessimism", "pity", "pleasure", "pride", "rage", "relief", "sadness", "satisfaction", "scorn", "shame", "sorrow", "sympathy", "terror", "unhappiness", "wonder", "wrath",
]

SPORTS = [
"amateur", "arena", "athletic", "backboard", "backhand", "batter (baseball)", "baseball", "basketball", "bench (noun)", "catcher (baseball)", "champion", "championship", "coach (noun)", "competitive", "defense", "doubles (tennis)", "dribble (verb)", "dugout", "fan", "field goal", "finish line", "football", "forehand", "free throw", "goal", "goal line", "goalkeeper", "goalpost", "grand slam", "half time", "hat trick", "hockey", "homeplate (baseball)", "homerun (baseball)", "infield (baseball)", "inning (baseball)", "jump shot (basketball)", "kickoff", "lay up (basketball)", "league", "locker room", "offense (noun)", "opponent", "outfield", "penalty", "pitcher (baseball)", "pro (noun)", "preseason", "puck (hockey)", "quarterback", "recreational", "referee", "score (noun)", "score (verb)", "scoreboard", "semifinal", "serve", "singles (tennis)", "soccer", "spectator sport", "sportscaster", "sportmanship", "stadium", "strike (noun)", "teammate", "tennis court", "tie (noun)", "time-out", "touchdown", "tournament", "track and field", "trainer", "trophy", "umpire", "underdog",
]

ENVIRONMENT = [
"aquifer", "atmosphere", "biodegradable", "biodiversity", "carbon dioxide", "carbon monoxide", "carcinogen", "climate", "coal", "compost (noun)", "compost (verb)", "conservation", "conservationist", "contaminant", "contamination", "deforestation", "disposable", "diversity", "ecology", "ecosystem", "emission", "endangered", "energy", "environment", "environmentalist", "erosion", "extinct", "extinction", "fossil fuel", "geothermal", "global warming", "green (adjective)", "greenhouse effect", "groundwater", "habitat", "herbicide", "landfill", "methane", "nuclear energy", "organic", "ozone layer", "pesticide", "petroleum", "pollutant", "pollution", "radiation", "rain forest", "recycle", "renewable", "smog", "solar", "sustainable", "toxic", "toxic waste", "waste", "wetland", "wildlife", "windmill",
]

EMPLOYMENT = [
"accountant", "actor", "actress", "air traffic controller", "architect", "artist", "athlete", "attorney", "banker", "bartender", "barber", "bookkeeper", "builder", "businessman", "businesswoman", "businessperson", "butcher", "carpenter", "cashier", "chef", "coach", "dental hygienist", "dentist", "designer", "developer", "dietician", "doctor", "economist", "editor", "electrician", "engineer", "farmer", "filmmaker", "fisherman", "flight attendant", "jeweler", "judge", "lawyer", "mechanic", "musician", "nutritionist", "nurse", "optician", "painter", "pharmacist", "photographer", "physician", "physician's assistant", "pilot", "plumber", "police officer", "politician", "professor", "programmer", "psychologist", "receptionist", "salesman", "salesperson", "saleswoman", "secretary", "singer", "surgeon", "teacher", "therapist", "translator", "translator", "undertaker", "veterinarian", "videographer", "waiter", "waitress", "writer",
]

FAMILY = [
"mother", "mom", "father", "dad", "parent", "children", "son", "daughter", "sister", "brother", "grandmother", "grandfather", "grandparent", "grandson", "granddaughter", "grandchild", "aunt", "uncle", "niece", "nephew", "cousin", "husband", "wife", "sister-in-law", "brother-in-law", "mother-in-law", "father-in-law", "partner", "fiancé", "fiancée", "stepmother", "stepfather", "ex",
]

BASKETBALL = [
"assist", "bracket", "center", "court", "defense", "dribble", "dunk", "forward", "foul", "guard", "press", "rebound", "rim", "swish", "upset", "zone",
]

BASEBALL = [
"average", "base", "bunt", "designate", "steal", "signal", "slug", "strike", "statistics", "rotation", "pastime", "roster", "foul", "series", "league", "pitch", "hustle", "dugout", "mound", "balk",
]

TOUCHING = [
"abrasive", "barbed", "bristle", "burnish", "coarse", "emollient", "glutinous", "hirsute", "lubricious", "plush", "slick", "thorny", "velvety", "viscous",
]

GOOD = [
"accomplished", "admirable", "attractive", "distinguished", "exceptional", "exemplary", "exquisite", "fine", "finest", "first-rate", "good", "great", "magnificent", "outstanding", "skillful", "sterling", "superb", "superlative", "capital", "certified", "champion", "choice", "choicest", "desirable", "distinctive", "estimable", "first", "first-class", "high", "incomparable", "invaluable", "meritorious", "notable", "noted", "peerless", "piked", "premium", "priceless", "prime", "select", "striking", "supreme", "tiptop", "top-notch", "transcendent", "world-class",
]

BAD = [
"bad", "common", "crude", "detestable", "ignorant", "inferior", "insignificant", "ordinary", "poor", "regular", "repulsive", "ugly", "unable", "unexceptional", "unknown", "unskilled", "failing", "imperfect", "indistinguished", "second-class", "second-rate", "unnoteworthy", "unworthy",
]

HELP = [
"advice", "aid", "benefit", "comfort", "cooperation", "guidance", "hand", "service", "support", "use", "assist", "avail", "balm", "corrective", "cure", "lift", "maintenance", "nourishment", "remedy", "succor", "sustenance", "utility", "helping hand",
]

_HELP = [
"blockage", "encumbrance", "handicap", "hindrance", "hurt", "injury", "obstruction", "prevention", "disease", "check", "counteraction", "harm", "management", "ownership", "stop",
]

