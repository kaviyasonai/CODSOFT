# WanderBot — Rule-Based Travel Guide Chatbot (Python Terminal)
### Task 1: Rule-Based Chatbot | Complete Documentation

---

## How to Run

1. Make sure Python 3.10 or above is installed on your laptop.
   Check by running:  python --version

2. Open CMD (Windows) or Terminal (Mac/Linux)

3. Navigate to the project folder:
   cd path\to\wanderbot_python

4. Run the chatbot:
   python main.py

That's it! No pip install needed — uses only Python built-in libraries.

---

## Project Structure

wanderbot_python/
|-- main.py       <- Entry point. Terminal UI, chat loop, colors
|-- engine.py     <- Rule-matching brain (normalize, match, respond)
|-- data.py       <- All destination data + general rules
|-- docs/
    |-- README.md <- This file

---

## How It Works — Step by Step

STEP 1  User types a message
STEP 2  main.py calls get_response(text) from engine.py
STEP 3  engine.py runs the pipeline:
           a) normalize()         -> clean the input
           b) find_destination()  -> detect country keyword
           c) detect_intent()     -> detect what user wants
           d) build response      -> combine data + intent
           e) fallback            -> if nothing matched
STEP 4  main.py prints the response with colors
STEP 5  Suggestions (followups) shown below response

---

## What You Can Ask

Destination info:
  "tell me about japan"
  "japan"

Packing tips:
  "packing for thailand"
  "what should i pack for dubai"

Visa info:
  "visa for japan"
  "do i need a visa for singapore"

Food guide:
  "food in italy"
  "what should i eat in france"

Budget:
  "how much does japan cost"
  "budget for maldives"

Best time:
  "best time to visit maldives"
  "when should i go to thailand"

Fun facts:
  "facts about australia"
  "interesting facts japan"

General:
  "help"
  "recommend a destination"
  "visa free countries"
  "bye"

Numbered shortcuts:
  After the bot shows suggestions [1] [2] [3] [4]
  just type the number to select that suggestion.

---

## Supported Destinations (10 countries)

Japan | France | India | Italy | Thailand
USA   | Australia | Dubai | Maldives | Singapore

---

## Concepts Used in This Project

Concept                  Where Used
-----------              ---------------------------
String normalization     normalize() in engine.py
Pattern matching         find_destination(), detect_intent()
if-else / match logic    detect_intent(), destination_response()
Dictionary data model    DESTINATIONS in data.py
List of rules            GENERAL_RULES in data.py
Functions                All files
Modules & imports        engine.py imports data.py
ANSI terminal colors     C class in main.py
while loop               Chat loop in main.py
Exception handling       KeyboardInterrupt in main.py
Random module            random.choice() for fallbacks
String formatting        f-strings throughout

---

## How to Add a New Destination

In data.py, add a new key inside the DESTINATIONS dictionary:

    "newzealand": {
        "flag": "",
        "capital": "Wellington",
        "currency": "NZ Dollar (NZ$)",
        "language": "English & Maori",
        "best_time": "December-February (summer)",
        "must_see": ["Milford Sound", "Hobbiton", "Rotorua"],
        "food": ["Hangi", "Pavlova", "Whitebait Fritters"],
        "packing": ["Waterproof jacket", "Hiking boots"],
        "visa": "Indians need a visitor visa.",
        "budget": "Mid-range: Rs.10,000-15,000/day.",
        "facts": ["NZ was the first country to give women the vote (1893)"],
        "tags": ["Nature", "Adventure", "Scenic"],
    },

No other changes needed — engine.py picks it up automatically!

---

## Sample Conversation

  WanderBot: Welcome aboard! I'm WanderBot...

  You: tell me about japan

  WanderBot:
    Japan  —  COMPLETE GUIDE
    ----------------------------------------
    Capital  : Tokyo
    Currency : Japanese Yen (Y)
    Language : Japanese
    Best time: March-May (cherry blossoms)...
    ...

  You: packing for japan

  WanderBot:
    PACKING GUIDE FOR JAPAN
    ----------------------------------------
    - Comfortable walking shoes
    - Pocket Wi-Fi or local SIM card
    ...

  You: 1   (shortcut for first suggestion)

  WanderBot:
    FUN FACTS ABOUT JAPAN
    ----------------------------------------
    - Japan has more vending machines per capita...
    ...

  You: bye

  WanderBot: Bon voyage! May your travels be full of adventure...
