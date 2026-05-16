_next_id = 0


def _poll(question, category, color, options_votes):
    global _next_id
    _next_id += 1
    options = [{"text": t, "votes": v} for t, v in options_votes]
    return {
        "id": _next_id,
        "question": question,
        "category": category,
        "color": color,
        "options": options,
        "total_votes": sum(o["votes"] for o in options),
    }


_RED   = "#e74c3c"
_BLUE  = "#2980b9"
_PURP  = "#8e44ad"
_GREEN = "#27ae60"
_PINK  = "#d63384"
_AMBER = "#e67e22"

ROWS = [
    {
        "title": "🔥 Trending Now",
        "color": _RED,
        "polls": [
            _poll("Is social media doing more harm than good?", "Trending", _RED, [
                ("Yes, definitely", 45123),
                ("No, it's beneficial", 18543),
                ("It depends", 67891),
                ("Not sure", 5234),
            ]),
            _poll("Cats or dogs?", "Trending", _RED, [
                ("Cats 🐱", 189234),
                ("Dogs 🐶", 223891),
                ("Both!", 56789),
                ("Neither", 8901),
            ]),
            _poll("4-day work week — should it be standard?", "Trending", _RED, [
                ("Absolutely, yes", 78923),
                ("No, it won't work", 12345),
                ("Depends on the job", 45678),
                ("Not feasible everywhere", 23456),
            ]),
            _poll("Best way to spend a Sunday?", "Trending", _RED, [
                ("Netflix & chill", 34521),
                ("Outdoors & active", 45678),
                ("Brunch with friends", 28901),
                ("Sleep all day", 67234),
            ]),
            _poll("Morning person or night owl?", "Trending", _RED, [
                ("Morning person ☀️", 89012),
                ("Night owl 🦉", 123456),
                ("Neither — just tired", 56789),
                ("Both somehow", 12345),
            ]),
            _poll("Best pizza topping?", "Trending", _RED, [
                ("Pepperoni", 145678),
                ("Margherita", 89012),
                ("BBQ Chicken", 67890),
                ("Hawaiian 🍍", 45231),
                ("Veggie", 34567),
            ]),
            _poll("Do you believe in work-life balance?", "Trending", _RED, [
                ("Yes, it's essential", 112345),
                ("Struggling with it", 89012),
                ("Work is my life", 23456),
                ("What's that?", 45678),
            ]),
            _poll("Preferred way to shop?", "Trending", _RED, [
                ("In-store", 56789),
                ("Online", 134567),
                ("Mix of both", 98765),
                ("Avoid shopping", 23456),
            ]),
        ],
    },
    {
        "title": "🏛️ Politics & Society",
        "color": _BLUE,
        "polls": [
            _poll("Most important global issue right now?", "Politics", _BLUE, [
                ("Climate change", 89012),
                ("AI safety & ethics", 45678),
                ("Economic inequality", 67890),
                ("Geopolitical tensions", 34521),
            ]),
            _poll("Should voting be mandatory?", "Politics", _BLUE, [
                ("Yes, it's a civic duty", 56789),
                ("No, it should be a choice", 78901),
                ("Yes, with exemptions", 34567),
                ("Undecided", 12345),
            ]),
            _poll("Best solution to housing affordability?", "Politics", _BLUE, [
                ("Government intervention", 34567),
                ("Free market solutions", 23456),
                ("Mixed approach", 56789),
                ("Tax reform", 19876),
            ]),
            _poll("Universal Basic Income — your take?", "Politics", _BLUE, [
                ("Strongly support", 45678),
                ("Somewhat support", 34567),
                ("Somewhat oppose", 23456),
                ("Strongly oppose", 34521),
            ]),
            _poll("Most trusted news source type?", "Politics", _BLUE, [
                ("Newspapers / Print", 23456),
                ("TV News", 34567),
                ("Online journalism", 45678),
                ("Podcasts", 56789),
                ("Social media", 12345),
            ]),
            _poll("Social media should be regulated like...", "Politics", _BLUE, [
                ("TV / Radio", 34567),
                ("Newspapers", 23456),
                ("Public utilities", 45678),
                ("Not at all", 56789),
            ]),
            _poll("Immigration: what's your view?", "Politics", _BLUE, [
                ("More open policies", 45678),
                ("Status quo is fine", 23456),
                ("More restrictive", 34567),
                ("Depends on context", 67890),
            ]),
        ],
    },
    {
        "title": "💻 Tech & Science",
        "color": _PURP,
        "polls": [
            _poll("Which AI assistant do you use most?", "Tech", _PURP, [
                ("ChatGPT", 189012),
                ("Claude", 134567),
                ("Gemini", 89012),
                ("Copilot", 45678),
                ("None", 34521),
            ]),
            _poll("Will AI take your job in 10 years?", "Tech", _PURP, [
                ("Definitely", 45678),
                ("Probably", 67890),
                ("Unlikely", 56789),
                ("No chance", 23456),
            ]),
            _poll("Favorite programming language?", "Tech", _PURP, [
                ("Python", 145678),
                ("JavaScript / TS", 123456),
                ("Rust", 45678),
                ("Go", 34567),
                ("Java", 23456),
            ]),
            _poll("Best smartphone OS?", "Tech", _PURP, [
                ("iOS", 234567),
                ("Android", 289012),
                ("Indifferent", 45678),
            ]),
            _poll("Are we living in a simulation?", "Tech", _PURP, [
                ("Yes, definitely", 34567),
                ("No", 56789),
                ("Maybe...", 89012),
                ("Interesting but irrelevant", 23456),
            ]),
            _poll("Should we colonise Mars?", "Tech", _PURP, [
                ("Absolutely, ASAP!", 67890),
                ("Focus on Earth first", 89012),
                ("Interesting but not urgent", 45678),
                ("No, too risky", 23456),
            ]),
            _poll("Electric vehicles — ready for mainstream?", "Tech", _PURP, [
                ("Already there", 56789),
                ("Almost ready", 78901),
                ("Still 5+ years away", 45678),
                ("Never fully mainstream", 12345),
            ]),
            _poll("Most impactful tech of the 21st century?", "Tech", _PURP, [
                ("Smartphones", 134567),
                ("The Internet", 189012),
                ("AI / Machine Learning", 145678),
                ("Social Media", 34567),
                ("Electric Vehicles", 23456),
            ]),
        ],
    },
    {
        "title": "⚽ Sports",
        "color": _GREEN,
        "polls": [
            _poll("Greatest footballer of all time?", "Sports", _GREEN, [
                ("Lionel Messi", 345678),
                ("Cristiano Ronaldo", 312345),
                ("Pelé", 89012),
                ("Maradona", 67890),
                ("Other", 23456),
            ]),
            _poll("Best sport to watch live?", "Sports", _GREEN, [
                ("Football / Soccer", 189012),
                ("Basketball", 123456),
                ("Tennis", 67890),
                ("Formula 1", 89012),
                ("Cricket", 56789),
            ]),
            _poll("Should eSports be in the Olympics?", "Sports", _GREEN, [
                ("Yes!", 134567),
                ("No", 89012),
                ("Maybe eventually", 67890),
                ("Don't care", 45678),
            ]),
            _poll("Premier League or Champions League?", "Sports", _GREEN, [
                ("Premier League", 145678),
                ("Champions League", 167890),
                ("Both equally", 89012),
                ("Neither", 12345),
            ]),
            _poll("Gym or outdoor exercise?", "Sports", _GREEN, [
                ("Gym 💪", 134567),
                ("Outdoors 🌿", 156789),
                ("Both", 89012),
                ("Neither 😅", 67890),
            ]),
            _poll("Best ever Olympic performance?", "Sports", _GREEN, [
                ("Usain Bolt 9.58s (2009)", 189012),
                ("Phelps — 8 golds in 2008", 145678),
                ("Simone Biles' gymnastics", 89012),
                ("Other", 34567),
            ]),
        ],
    },
    {
        "title": "🎬 Entertainment",
        "color": _PINK,
        "polls": [
            _poll("Best decade for music?", "Entertainment", _PINK, [
                ("70s", 45678),
                ("80s", 89012),
                ("90s", 145678),
                ("2000s", 67890),
                ("2010s+", 89012),
            ]),
            _poll("Marvel or DC?", "Entertainment", _PINK, [
                ("Marvel 🦸", 234567),
                ("DC 🦇", 123456),
                ("Neither", 45678),
                ("Both equally", 56789),
            ]),
            _poll("Best streaming platform?", "Entertainment", _PINK, [
                ("Netflix", 234567),
                ("Disney+", 89012),
                ("HBO Max", 123456),
                ("Amazon Prime", 67890),
                ("Apple TV+", 34567),
            ]),
            _poll("Prefer to watch movies...", "Entertainment", _PINK, [
                ("At the cinema", 134567),
                ("At home", 189012),
                ("Either is fine", 89012),
                ("I don't watch movies", 12345),
            ]),
            _poll("Best music genre?", "Entertainment", _PINK, [
                ("Pop", 145678),
                ("Hip-Hop / Rap", 189012),
                ("Rock", 123456),
                ("Electronic / EDM", 67890),
                ("R&B / Soul", 89012),
            ]),
            _poll("Books or TV shows?", "Entertainment", _PINK, [
                ("Books 📚", 134567),
                ("TV Shows 📺", 189012),
                ("Both!", 145678),
                ("Neither", 23456),
            ]),
            _poll("Most anticipated film genre of 2026?", "Entertainment", _PINK, [
                ("Sci-Fi", 89012),
                ("Action / Superhero", 123456),
                ("Drama / Thriller", 78901),
                ("Horror", 56789),
                ("Animation", 67890),
            ]),
        ],
    },
    {
        "title": "🍕 Food & Lifestyle",
        "color": _AMBER,
        "polls": [
            _poll("Best cuisine in the world?", "Food", _AMBER, [
                ("Italian 🍝", 189012),
                ("Japanese 🍣", 167890),
                ("Mexican 🌮", 134567),
                ("Indian 🍛", 145678),
                ("French 🥐", 56789),
                ("Thai 🍜", 89012),
            ]),
            _poll("Coffee or tea?", "Food", _AMBER, [
                ("Coffee ☕", 345678),
                ("Tea 🍵", 234567),
                ("Both!", 89012),
                ("Neither", 34567),
            ]),
            _poll("Vegan, vegetarian or meat-eater?", "Food", _AMBER, [
                ("Vegan 🌱", 67890),
                ("Vegetarian", 89012),
                ("Flexitarian", 123456),
                ("Meat-eater 🥩", 234567),
            ]),
            _poll("Best meal of the day?", "Food", _AMBER, [
                ("Breakfast", 145678),
                ("Lunch", 89012),
                ("Dinner", 234567),
                ("Late-night snack", 78901),
            ]),
            _poll("Preferred breakfast?", "Food", _AMBER, [
                ("Full cooked breakfast", 89012),
                ("Cereal / Granola", 123456),
                ("Toast / Pastry", 145678),
                ("Skip it entirely", 67890),
            ]),
            _poll("Beer, wine, or cocktails?", "Food", _AMBER, [
                ("Beer 🍺", 134567),
                ("Wine 🍷", 145678),
                ("Cocktails 🍹", 89012),
                ("Non-alcoholic for me", 78901),
            ]),
            _poll("Best fast food chain?", "Food", _AMBER, [
                ("McDonald's", 189012),
                ("Burger King", 67890),
                ("KFC", 89012),
                ("Subway", 78901),
                ("Chipotle", 123456),
            ]),
        ],
    },
]

_BY_ID: dict[int, dict] = {}
for _row in ROWS:
    for _poll in _row["polls"]:
        _BY_ID[_poll["id"]] = _poll


def get_poll(poll_id: int) -> dict | None:
    return _BY_ID.get(poll_id)
