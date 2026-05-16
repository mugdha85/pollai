# PollAI — UI

A Netflix-style polling interface built with Flask. Polls are organised into thematic rows; each card is clickable and lets you vote and see live results.

---

## What it looks like

- **Sticky navbar** with frosted-glass blur
- **Hero banner** showing total votes, active polls, and category count
- **Six horizontally scrollable rows**, each with a colour-coded accent:
  - 🔥 Trending Now
  - 🏛️ Politics & Society
  - 💻 Tech & Science
  - ⚽ Sports
  - 🎬 Entertainment
  - 🍕 Food & Lifestyle
- **Poll cards** that lift on hover and reveal a "Vote →" CTA
- **Voting modal** with animated progress bars and per-category colour theming

---

## Project structure

```
src/pollai/
├── app.py                  Flask app and vote API
├── data.py                 48 dummy polls across 6 rows
├── templates/
│   └── index.html          Jinja2 template (Netflix-style layout)
└── static/
    ├── style.css           Light/clean theme, responsive
    └── main.js             Vote submission, modal, scroll controls
```

---

## Running locally

**Prerequisites:** Python 3.12+, pip

1. Install Flask:

   ```bash
   pip install flask
   ```

2. Start the dev server from the project root:

   ```bash
   PYTHONPATH=src flask --app pollai.app run --debug --port 5000
   ```

   On Windows (PowerShell):

   ```powershell
   $env:PYTHONPATH = "src"; python -m flask --app pollai.app run --debug --port 5000
   ```

3. Open [http://localhost:5000](http://localhost:5000)

---

## How voting works

Clicking a poll card opens a modal. Selecting an option sends a `POST` to:

```
/api/vote/<poll_id>/<option_index>
```

The server increments the in-memory vote count and returns updated percentages. The modal then renders animated progress bars. The leading option is highlighted in the row's accent colour.

> Votes are held in memory and reset on server restart. Persistence (database, file, etc.) is not yet implemented.

---

## Adding or editing polls

All poll content lives in `src/pollai/data.py`. Each row is a dict with a `title`, a hex `color`, and a list of polls built with the `_poll()` helper:

```python
_poll(
    "Your question here?",
    "Category label",
    "#hexcolor",
    [
        ("Option A", 1000),   # (text, seed vote count)
        ("Option B", 800),
        ("Option C", 600),
    ],
)
```

Add the new poll to the relevant row's `"polls"` list (or create a new row) and restart the server.

---

## Tech stack

| Layer     | Choice                        |
|-----------|-------------------------------|
| Server    | Flask 3.x                     |
| Templating| Jinja2 (via Flask)            |
| Styling   | Vanilla CSS (custom properties, flexbox) |
| JS        | Vanilla JS (no framework)     |
| Fonts     | Inter via Google Fonts        |
| Data      | In-memory Python dicts        |
