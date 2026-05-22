# ============================================================
#  WanderBot — data.py
#  All destination data and general rules
# ============================================================

# Each destination has 8 fields of travel information.
# To add a new country, copy any block and fill in your values.

DESTINATIONS = {
    "japan": {
        "flag": "🇯🇵",
        "capital": "Tokyo",
        "currency": "Japanese Yen (¥)",
        "language": "Japanese",
        "best_time": "March–May (cherry blossoms) or Oct–Nov (autumn foliage)",
        "must_see": [
            "Mount Fuji",
            "Kyoto Temples",
            "Shibuya Crossing",
            "Hiroshima Peace Park",
            "Arashiyama Bamboo Grove",
        ],
        "food": ["Sushi", "Ramen", "Takoyaki", "Matcha desserts", "Tempura"],
        "packing": [
            "Comfortable walking shoes",
            "Pocket Wi-Fi or local SIM card",
            "IC card for public transit",
            "Cash (Japan is still very cash-heavy)",
            "Light layers for seasonal temperature changes",
        ],
        "visa": "Indians need a visa. Apply at the Japanese consulate. Processing ~5 business days.",
        "budget": "Mid-range: Rs.5,000-8,000/day. Budget hostels from Rs.1,500/night.",
        "facts": [
            "Japan has more vending machines per capita than any other country",
            "There are more pets than children in Japan",
            "Japanese trains are accurate to the second",
            "Japan has 14 UNESCO World Heritage Sites",
        ],
        "tags": ["Culture", "Temples", "Food", "Nature", "Tech"],
    },
    "france": {
        "flag": "🇫🇷",
        "capital": "Paris",
        "currency": "Euro (€)",
        "language": "French",
        "best_time": "April–June or September–October (mild weather, fewer crowds)",
        "must_see": [
            "Eiffel Tower",
            "Louvre Museum",
            "Mont Saint-Michel",
            "French Riviera",
            "Palace of Versailles",
        ],
        "food": ["Croissants", "Baguettes", "Coq au vin", "Crepes", "Cheese & wine"],
        "packing": [
            "Stylish but comfortable clothes",
            "Universal travel adapter",
            "French phrasebook or translation app",
            "Good walking shoes (cobblestones!)",
            "Reusable tote bag",
        ],
        "visa": "Indians need a Schengen visa. Apply at the French consulate at least 15 days before travel.",
        "budget": "Mid-range: Rs.8,000-12,000/day. Budget hostels from Rs.2,000/night.",
        "facts": [
            "France is the most visited country in the world",
            "The Louvre is the world's most visited museum",
            "France has 45 UNESCO World Heritage Sites",
            "French people consume an average of 26 kg of cheese per person per year",
        ],
        "tags": ["Romance", "Art", "Food", "History", "Fashion"],
    },
    "india": {
        "flag": "🇮🇳",
        "capital": "New Delhi",
        "currency": "Indian Rupee (Rs.)",
        "language": "Hindi and 21 other official languages",
        "best_time": "October–March (cool and dry across most regions)",
        "must_see": [
            "Taj Mahal, Agra",
            "Kerala Backwaters",
            "Rajasthan Forts & Palaces",
            "Varanasi Ghats",
            "Himalayas & Ladakh",
        ],
        "food": ["Biryani", "Butter Chicken", "Masala Dosa", "Street Chaat", "Chai"],
        "packing": [
            "Light cotton clothes (breathable)",
            "High-SPF sunscreen",
            "Basic stomach medicines",
            "Modest attire for temples & mosques",
            "Insect repellent for south & northeast",
        ],
        "visa": "No visa needed for Indian citizens! Domestic travel only — just pack and go.",
        "budget": "Budget: Rs.1,500-3,000/day. Mid-range: Rs.4,000-7,000/day.",
        "facts": [
            "India has the world's largest road network after the US and China",
            "Chess was invented in India around the 6th century",
            "India has the world's most vegetarians",
            "The number zero was invented by Indian mathematician Brahmagupta",
        ],
        "tags": ["Heritage", "Spirituality", "Food", "Diversity", "Adventure"],
    },
    "thailand": {
        "flag": "🇹🇭",
        "capital": "Bangkok",
        "currency": "Thai Baht (฿)",
        "language": "Thai",
        "best_time": "November–April (dry season)",
        "must_see": [
            "Grand Palace, Bangkok",
            "Chiang Mai Temples",
            "Phi Phi Islands",
            "Elephant Nature Park",
            "Floating Markets",
        ],
        "food": ["Pad Thai", "Tom Yum Soup", "Mango Sticky Rice", "Green Curry", "Som Tum"],
        "packing": [
            "Light breathable clothes (hot and humid)",
            "Mosquito repellent",
            "Reef-safe sunscreen for islands",
            "Flip flops or sandals",
            "Temple cover-up (sarong)",
        ],
        "visa": "Indians get 30-day visa on arrival (free). E-visa also available online.",
        "budget": "Budget: Rs.2,000-4,000/day. Very affordable! Street food from Rs.50/meal.",
        "facts": [
            "Thailand is called 'The Land of Smiles'",
            "It is illegal to step on Thai currency — it bears the king's image",
            "Thailand has never been colonized by a European power",
            "There are over 35,000 Buddhist temples in Thailand",
        ],
        "tags": ["Beaches", "Temples", "Street Food", "Budget-friendly", "Nightlife"],
    },
    "dubai": {
        "flag": "🇦🇪",
        "capital": "Abu Dhabi (Dubai is the most famous city)",
        "currency": "UAE Dirham (AED)",
        "language": "Arabic (English widely spoken)",
        "best_time": "November–March (pleasant 20-28°C)",
        "must_see": [
            "Burj Khalifa",
            "Dubai Mall & Dubai Fountain",
            "Palm Jumeirah",
            "Desert Safari",
            "Gold Souk & Spice Souk",
        ],
        "food": ["Shawarma", "Al Harees", "Camel Milk Ice Cream", "Luqaimat", "Arabic Mezze"],
        "packing": [
            "Modest clothing for souks and mosques",
            "High SPF sunscreen",
            "Light summer clothes",
            "Swimwear for hotel pools",
            "Comfortable sandals",
        ],
        "visa": "Indians with valid US/UK/EU visa get free visa on arrival. Others apply online for UAE tourist visa.",
        "budget": "Mid-range: Rs.8,000-15,000/day. Many luxury options available.",
        "facts": [
            "Dubai went from a fishing village to global metropolis in under 50 years",
            "The Burj Khalifa has 163 floors and stands 828 metres tall",
            "Dubai has an indoor ski slope in the middle of the desert (Ski Dubai)",
            "Gold ATMs exist in Dubai malls — buy gold bars from a machine!",
        ],
        "tags": ["Luxury", "Shopping", "Desert", "Architecture", "Nightlife"],
    },
    "maldives": {
        "flag": "🇲🇻",
        "capital": "Male",
        "currency": "Maldivian Rufiyaa (MVR)",
        "language": "Dhivehi (English widely spoken in resorts)",
        "best_time": "November–April (dry season, best for diving)",
        "must_see": [
            "Overwater Bungalows",
            "Coral Reef Snorkeling",
            "Bioluminescent Beaches (Vaadhoo Island)",
            "Male Fish Market",
            "Banana Reef Diving",
        ],
        "food": ["Mas Huni (tuna & coconut)", "Garudhiya Fish Soup", "Hedhikaa Snacks", "Fresh Tropical Fruits", "Grilled Lobster"],
        "packing": [
            "Reef-safe sunscreen (protects coral reefs)",
            "Snorkel gear (or rent at resort)",
            "Light linen & cotton clothes",
            "Water shoes for reef walking",
            "Underwater camera or GoPro",
        ],
        "visa": "Indians get free 30-day visa on arrival. No prior application needed.",
        "budget": "Guesthouses: Rs.5,000-8,000/day. Luxury water villas: Rs.30,000-80,000/day.",
        "facts": [
            "The Maldives is the lowest-lying country in the world (avg 1.5m above sea level)",
            "It consists of 1,200 islands spread across 90,000 sq km of ocean",
            "Bioluminescent plankton makes beach waves glow blue at night",
            "The Maldives has some of the clearest water in the world (80m visibility)",
        ],
        "tags": ["Luxury", "Beaches", "Diving", "Romance", "Island Life"],
    },
    "singapore": {
        "flag": "🇸🇬",
        "capital": "Singapore (city-state)",
        "currency": "Singapore Dollar (S$)",
        "language": "English, Mandarin, Malay, Tamil",
        "best_time": "February–April (least rainfall)",
        "must_see": [
            "Gardens by the Bay",
            "Marina Bay Sands",
            "Sentosa Island",
            "Hawker Centres",
            "Universal Studios Singapore",
        ],
        "food": ["Hainanese Chicken Rice", "Laksa", "Char Kway Teow", "Chilli Crab", "Kaya Toast"],
        "packing": [
            "Light clothes (hot and humid year-round, 28-34°C)",
            "Compact umbrella (sudden tropical showers)",
            "Comfortable walking shoes",
            "Note: Chewing gum is banned in Singapore!",
            "EZ-Link card for MRT and bus",
        ],
        "visa": "Indians get free 30-day visa on arrival.",
        "budget": "Mid-range: Rs.7,000-12,000/day. Hawker food very affordable (Rs.200-400/meal).",
        "facts": [
            "Singapore has zero natural resources yet is one of the top 10 richest countries",
            "Chewing gum is banned — you can be fined for bringing it in",
            "It is one of only three city-states in the world",
            "Changi Airport has a 40-metre indoor waterfall and butterfly garden — both free",
        ],
        "tags": ["City", "Food", "Shopping", "Family", "Clean & Safe"],
    },
    "australia": {
        "flag": "🇦🇺",
        "capital": "Canberra",
        "currency": "Australian Dollar (A$)",
        "language": "English",
        "best_time": "September–November (spring) or March–May (autumn)",
        "must_see": [
            "Great Barrier Reef",
            "Sydney Opera House",
            "Uluru (Ayers Rock)",
            "Great Ocean Road",
            "Daintree Rainforest",
        ],
        "food": ["Vegemite on Toast", "Tim Tams", "Meat Pie", "Pavlova", "Barramundi"],
        "packing": [
            "SPF 50+ sunscreen (Australian UV is extreme)",
            "Insect repellent",
            "Sturdy hiking shoes",
            "Swimwear",
            "Light rain jacket",
        ],
        "visa": "Indians need an ETA (Electronic Travel Authority) or tourist visa. Apply online.",
        "budget": "Mid-range: Rs.10,000-16,000/day.",
        "facts": [
            "Australia is the only continent that is also a single country",
            "Kangaroos outnumber humans 2:1",
            "Australia has over 10,000 beaches",
            "The Great Barrier Reef is visible from space",
        ],
        "tags": ["Wildlife", "Beaches", "Adventure", "Nature", "Cities"],
    },
    "italy": {
        "flag": "🇮🇹",
        "capital": "Rome",
        "currency": "Euro (€)",
        "language": "Italian",
        "best_time": "April–June or September–October",
        "must_see": [
            "Colosseum, Rome",
            "Venice Canals & Gondolas",
            "Amalfi Coast",
            "Florence Duomo",
            "Cinque Terre",
        ],
        "food": ["Pizza Napoletana", "Pasta Carbonara", "Gelato", "Tiramisu", "Risotto"],
        "packing": [
            "Very comfortable walking shoes (cobblestones everywhere!)",
            "Modesty cover for churches (no bare shoulders/knees)",
            "Sunglasses & SPF sunscreen",
            "Small lightweight daypack",
            "Offline maps",
        ],
        "visa": "Indians need a Schengen visa. Apply at the Italian consulate.",
        "budget": "Mid-range: Rs.7,000-11,000/day.",
        "facts": [
            "Italy has more UNESCO World Heritage Sites than any other country (58!)",
            "Italy invented the piano, radio, and eyeglasses",
            "Pizza was invented in Naples around the 18th century",
            "Rome has more fountains than any other city in the world",
        ],
        "tags": ["History", "Food", "Art", "Romance", "Architecture"],
    },
    "usa": {
        "flag": "🇺🇸",
        "capital": "Washington D.C.",
        "currency": "US Dollar ($)",
        "language": "English",
        "best_time": "Spring (Apr–May) or Fall (Sep–Oct) — varies by region",
        "must_see": [
            "Grand Canyon, Arizona",
            "New York City",
            "Yellowstone National Park",
            "Yosemite, California",
            "New Orleans",
        ],
        "food": ["BBQ Ribs", "Clam Chowder", "Tex-Mex", "Lobster Rolls", "Chicago Deep-dish Pizza"],
        "packing": [
            "Comfortable sneakers for city walking",
            "Cash for tipping (15-20% is standard)",
            "Comprehensive travel insurance",
            "Power bank",
            "Type A/B adapter if needed",
        ],
        "visa": "Indians need a B1/B2 tourist visa. Apply well in advance — wait times can be 6-12 months.",
        "budget": "Mid-range: Rs.12,000-20,000/day depending on city.",
        "facts": [
            "The US has 63 national parks covering over 52 million acres",
            "Americans consume 100 acres of pizza per day",
            "The Library of Congress is the largest library in the world",
            "Alaska has more coastline than all other US states combined",
        ],
        "tags": ["Road Trips", "Nature", "Cities", "Adventure", "Diversity"],
    },
}

# ── GENERAL RULES ─────────────────────────────────────────────
# Each rule: { "patterns": [...], "response": "..." , "followups": [...] }
# Patterns are checked using keyword-in-string matching.

GENERAL_RULES = [
    {
        "patterns": ["hello", "hi", "hey", "howdy", "greetings", "help", "start", "what can you do"],
        "response": (
            "Hey there, traveller!  I'm WanderBot, your personal travel guide.\n\n"
            "Here's what I can help you with:\n"
            "  [MAP]      Destination info (must-see, food, facts)\n"
            "  [BAG]      Packing tips for any country\n"
            "  [MONEY]    Budget estimates in INR\n"
            "  [PASSPORT] Visa information for Indians\n"
            "  [CALENDAR] Best time to visit\n"
            "  [STAR]     Fun & surprising travel facts\n\n"
            "Just type a country name or ask naturally!\n"
            "Try: 'tell me about japan'  or  'packing tips for thailand'"
        ),
        "followups": ["japan", "thailand", "maldives", "dubai"],
    },
    {
        "patterns": ["budget", "cheap", "affordable", "cost", "money", "price", "how much", "expensive"],
        "response": (
            "BUDGET OVERVIEW BY REGION\n"
            + "-" * 35 + "\n"
            "GREEN  Budget-friendly:\n"
            "  Thailand    -> Rs.2,000-4,000/day\n"
            "  India       -> Rs.1,500-3,000/day\n"
            "  Singapore   -> Rs.7,000/day\n\n"
            "YELLOW Mid-range:\n"
            "  Japan       -> Rs.5,000-8,000/day\n"
            "  Dubai       -> Rs.8,000-15,000/day\n"
            "  France/Italy-> Rs.8,000-12,000/day\n\n"
            "RED    Premium:\n"
            "  USA         -> Rs.12,000-20,000/day\n"
            "  Australia   -> Rs.10,000-16,000/day\n"
            "  Maldives    -> Rs.30,000+/day (resorts)\n\n"
            "Ask me about a specific country for more detail!"
        ),
        "followups": ["thailand", "japan", "maldives"],
    },
    {
        "patterns": ["visa", "passport", "entry", "permit", "visa free", "visa on arrival"],
        "response": (
            "VISA INFO FOR INDIAN PASSPORT HOLDERS\n"
            + "-" * 38 + "\n"
            "FREE / VISA ON ARRIVAL:\n"
            "  Thailand  -> 30 days free\n"
            "  Maldives  -> 30 days free\n"
            "  Singapore -> 30 days free\n"
            "  Dubai     -> free (with valid US/UK/EU visa)\n"
            "  Indonesia -> 30 days free\n\n"
            "VISA REQUIRED (apply in advance):\n"
            "  Japan       -> Apply at Japanese consulate\n"
            "  France/Italy-> Schengen visa\n"
            "  USA         -> B1/B2 visa (long wait times!)\n"
            "  Australia   -> ETA or tourist visa\n\n"
            "Ask about a specific country for more detail!"
        ),
        "followups": ["japan", "singapore", "usa"],
    },
    {
        "patterns": ["best time", "when to visit", "season", "weather", "monsoon", "when should i go"],
        "response": (
            "BEST TIMES TO VISIT\n"
            + "-" * 30 + "\n"
            "SPRING:\n"
            "  Japan   -> March-May (cherry blossoms!)\n"
            "  France  -> April-June\n\n"
            "DRY SEASON:\n"
            "  Thailand -> November-April\n"
            "  Maldives -> November-April\n"
            "  Dubai    -> November-March\n\n"
            "PLEASANT AUTUMN:\n"
            "  Italy    -> September-October\n"
            "  USA      -> September-October\n\n"
            "YEAR-ROUND:\n"
            "  Singapore (tropical, always warm)\n"
            "  Dubai (hot but always open!)\n\n"
            "Type a country name for specific advice!"
        ),
        "followups": ["japan", "maldives", "italy"],
    },
    {
        "patterns": ["packing", "what to bring", "luggage", "bag", "carry", "essentials", "checklist"],
        "response": (
            "UNIVERSAL PACKING ESSENTIALS\n"
            + "-" * 30 + "\n"
            "DOCUMENTS:\n"
            "  - Passport + photocopies\n"
            "  - Visa & travel insurance\n"
            "  - Emergency contacts list\n\n"
            "HEALTH:\n"
            "  - Basic first aid kit\n"
            "  - Personal medications\n"
            "  - ORS & stomach tablets\n\n"
            "TECH:\n"
            "  - Universal power adapter\n"
            "  - Power bank (10,000 mAh+)\n"
            "  - Offline maps downloaded\n\n"
            "CLOTHING:\n"
            "  - Layers for temperature changes\n"
            "  - 1 smart outfit\n"
            "  - Comfortable walking shoes\n\n"
            "Type 'packing for [country]' for specific tips!"
        ),
        "followups": ["packing for japan", "packing for thailand", "packing for maldives"],
    },
    {
        "patterns": ["food", "eat", "cuisine", "dish", "must eat", "local food", "taste"],
        "response": (
            "MUST-TRY FOODS AROUND THE WORLD\n"
            + "-" * 33 + "\n"
            "Japan     -> Ramen, Sushi, Matcha\n"
            "Thailand  -> Pad Thai, Tom Yum, Mango Sticky Rice\n"
            "Italy     -> Pizza, Pasta Carbonara, Gelato\n"
            "France    -> Croissants, Cheese, Crepes\n"
            "India     -> Biryani, Butter Chicken, Dosa\n"
            "Dubai     -> Shawarma, Arabic Mezze\n"
            "Singapore -> Chicken Rice, Laksa, Chilli Crab\n"
            "Maldives  -> Fresh Lobster, Mas Huni\n\n"
            "Type a country name for its full food guide!"
        ),
        "followups": ["food in japan", "food in singapore", "food in thailand"],
    },
    {
        "patterns": ["fact", "facts", "trivia", "interesting", "did you know", "surprising", "weird"],
        "response": (
            "RANDOM TRAVEL FACTS\n"
            + "-" * 30 + "\n"
            "- Japan has more vending machines per capita than any country\n"
            "- France is the MOST visited country in the world\n"
            "- Italy has MORE UNESCO sites than any country (58!)\n"
            "- Dubai went from desert to skyscrapers in just 50 years\n"
            "- Maldives beaches GLOW blue at night (bioluminescent plankton!)\n"
            "- Singapore's Changi Airport has a 40m waterfall inside — free!\n"
            "- Australia has more kangaroos than people (2:1 ratio!)\n\n"
            "Type 'facts about [country]' for destination-specific trivia!"
        ),
        "followups": ["facts about japan", "facts about maldives", "facts about australia"],
    },
    {
        "patterns": ["recommend", "suggest", "where should i go", "best destination", "where to go", "popular"],
        "response": (
            "TOP DESTINATION RECOMMENDATIONS\n"
            + "-" * 33 + "\n"
            "First-time international travellers:\n"
            "  -> Thailand or Singapore\n\n"
            "Beach lovers:\n"
            "  -> Maldives or Thailand islands\n\n"
            "History & culture:\n"
            "  -> Japan, Italy, or India\n\n"
            "Luxury & shopping:\n"
            "  -> Dubai or Singapore\n\n"
            "Nature & wildlife:\n"
            "  -> Australia\n\n"
            "Romance:\n"
            "  -> France, Italy, or Maldives\n\n"
            "Want full details? Type any country name!"
        ),
        "followups": ["thailand", "maldives", "japan"],
    },
    {
        "patterns": ["thanks", "thank you", "thx", "ty", "great", "awesome", "helpful", "nice", "good bot"],
        "response": "You're welcome! Safe travels and happy exploring! Is there another destination you'd like to know about?",
        "followups": ["japan", "best time to visit", "visa information"],
    },
    {
        "patterns": ["bye", "goodbye", "exit", "quit", "see you", "cya", "farewell"],
        "response": "Bon voyage! May your travels be full of adventure and wonderful memories. Come back anytime!\n[EXIT]",
        "followups": [],
    },
]
