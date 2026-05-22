# ============================================================
#  WanderBot — engine.py
#  Core rule-matching logic — the "brain" of the chatbot
#
#  PIPELINE:
#  1. normalize(text)        -> clean input
#  2. find_destination(text) -> detect country keyword
#  3. detect_intent(text)    -> detect what user wants
#  4. build_response()       -> combine destination + intent
#  5. fallback               -> if nothing matched
# ============================================================

import re
import random
from data import DESTINATIONS, GENERAL_RULES


# ── STEP 1: NORMALIZE ────────────────────────────────────────
def normalize(text: str) -> str:
    """
    Converts raw user input into a clean matchable string.
    Examples:
        "Hello!!!"         -> "hello"
        "JAPAN??"          -> "japan"
        "Packing for JAPAN??" -> "packing for japan"
    """
    text = text.lower()                        # lowercase
    text = re.sub(r"[^\w\s]", "", text)        # remove punctuation
    text = text.strip()                        # strip whitespace
    return text


# ── STEP 2: FIND DESTINATION ─────────────────────────────────
def find_destination(norm_input: str) -> str | None:
    """
    Scans normalized input for a known destination keyword.
    Returns the matched key (e.g. 'japan') or None.
    Uses simple keyword-in-string matching.
    """
    for key in DESTINATIONS:
        if key in norm_input:
            return key
    return None


# ── STEP 3: DETECT INTENT ────────────────────────────────────
def detect_intent(norm_input: str) -> str:
    """
    Returns one of:
        'packing' | 'facts' | 'food' | 'visa' | 'budget' |
        'best_time' | 'must_see' | 'general'

    Checked in order — most specific patterns first.
    """
    if any(kw in norm_input for kw in ["pack", "bring", "luggage", "bag", "carry", "essentials"]):
        return "packing"

    if any(kw in norm_input for kw in ["fact", "trivia", "interesting", "did you know", "surprising"]):
        return "facts"

    if any(kw in norm_input for kw in ["food", "eat", "cuisine", "dish", "must eat", "taste", "restaurant"]):
        return "food"

    if any(kw in norm_input for kw in ["visa", "passport", "entry", "permit", "document"]):
        return "visa"

    if any(kw in norm_input for kw in ["budget", "cost", "cheap", "price", "how much", "money", "expensive"]):
        return "budget"

    if any(kw in norm_input for kw in ["best time", "when", "season", "weather", "month", "monsoon"]):
        return "best_time"

    if any(kw in norm_input for kw in ["see", "visit", "place", "attraction", "must", "spot", "go"]):
        return "must_see"

    return "general"


# ── STEP 4: BUILD DESTINATION RESPONSE ───────────────────────
def destination_response(key: str, intent: str) -> tuple[str, list]:
    """
    Combines destination data + intent to produce a response.
    Returns (response_text, followups_list)
    """
    d = DESTINATIONS[key]
    name = key.capitalize()
    header = f"{d['flag']}  {name}"
    sep = "-" * 40

    if intent == "packing":
        items = "\n".join(f"  - {p}" for p in d["packing"])
        text = (
            f"PACKING GUIDE FOR {name.upper()}\n{sep}\n"
            f"{items}\n\n"
            f"Best time to visit: {d['best_time']}\n"
            f"Budget: {d['budget']}"
        )
        return text, [f"facts about {key}", f"food in {key}", f"visa for {key}"]

    elif intent == "facts":
        items = "\n".join(f"  - {f}" for f in d["facts"])
        text = (
            f"FUN FACTS ABOUT {name.upper()}\n{sep}\n"
            f"{items}\n\n"
            f"Tags: {' | '.join(d['tags'])}"
        )
        return text, [f"tell me about {key}", f"food in {key}", f"packing for {key}"]

    elif intent == "food":
        items = "\n".join(f"  - {f}" for f in d["food"])
        text = (
            f"MUST-TRY FOOD IN {name.upper()}\n{sep}\n"
            f"{items}\n\n"
            f"Tip: Ask locals for the best spots — avoid tourist traps near main attractions!"
        )
        return text, [f"packing for {key}", f"facts about {key}", f"best time for {key}"]

    elif intent == "visa":
        text = (
            f"VISA INFO FOR {name.upper()}\n{sep}\n"
            f"{d['visa']}\n\n"
            f"Language: {d['language']}\n"
            f"Currency: {d['currency']}"
        )
        return text, [f"budget for {key}", f"tell me about {key}", f"packing for {key}"]

    elif intent == "budget":
        text = (
            f"BUDGET GUIDE FOR {name.upper()}\n{sep}\n"
            f"{d['budget']}\n\n"
            f"Currency: {d['currency']}\n"
            f"Visa: {d['visa']}"
        )
        return text, [f"packing for {key}", f"best time for {key}", f"food in {key}"]

    elif intent == "best_time":
        text = (
            f"BEST TIME TO VISIT {name.upper()}\n{sep}\n"
            f"{d['best_time']}\n\n"
            f"Tip: Book flights 2-3 months early for peak season discounts!"
        )
        return text, [f"packing for {key}", f"visa for {key}", f"facts about {key}"]

    elif intent == "must_see":
        items = "\n".join(f"  -> {p}" for p in d["must_see"])
        text = (
            f"MUST-SEE PLACES IN {name.upper()}\n{sep}\n"
            f"{items}\n\n"
            f"Tags: {' | '.join(d['tags'])}"
        )
        return text, [f"food in {key}", f"packing for {key}", f"facts about {key}"]

    else:  # general — full overview
        must_see = "\n".join(f"  -> {p}" for p in d["must_see"][:3])
        food = ", ".join(d["food"][:3])
        text = (
            f"{header}  —  COMPLETE GUIDE\n{sep}\n"
            f"Capital  : {d['capital']}\n"
            f"Currency : {d['currency']}\n"
            f"Language : {d['language']}\n"
            f"Best time: {d['best_time']}\n\n"
            f"Must-see places:\n{must_see}\n\n"
            f"Local food: {food}\n\n"
            f"Visa    : {d['visa']}\n"
            f"Budget  : {d['budget']}"
        )
        return text, [f"packing for {key}", f"facts about {key}", f"food in {key}"]


# ── STEP 5: FALLBACK RESPONSES ───────────────────────────────
FALLBACKS = [
    (
        "Hmm, I couldn't find info on that.\n\n"
        "I cover these destinations:\n"
        "  Japan | France | India | Italy | Thailand\n"
        "  USA   | Australia | Dubai | Maldives | Singapore\n\n"
        "Or ask: 'best time to visit' | 'visa info' | 'packing tips' | 'food recommendations'"
    ),
    (
        "My pattern matching didn't find a match. Try rephrasing!\n\n"
        "Examples:\n"
        "  - 'Tell me about France'\n"
        "  - 'Packing list for Dubai'\n"
        "  - 'Visa requirements for Japan'\n"
        "  - 'Best time to visit Maldives'"
    ),
    (
        "I don't have a rule for that yet!\n\n"
        "Try: 'tell me about japan'  or  'packing tips for thailand'\n"
        "Type 'help' to see everything I can do."
    ),
]


# ── MAIN ENTRY: get_response() ───────────────────────────────
def get_response(user_input: str) -> tuple[str, list]:
    """
    Full pipeline: normalize -> find destination ->
    detect intent -> build response -> fallback.

    Returns (response_text, followups_list)
    """
    norm = normalize(user_input)

    # 1. Try destination match (most specific)
    dest = find_destination(norm)
    if dest:
        intent = detect_intent(norm)
        return destination_response(dest, intent)

    # 2. Try general rules (broad topic questions)
    for rule in GENERAL_RULES:
        if any(pattern in norm for pattern in rule["patterns"]):
            return rule["response"], rule["followups"]

    # 3. Nothing matched — random fallback
    return random.choice(FALLBACKS), ["help", "japan", "visa information", "packing tips"]
