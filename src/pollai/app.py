from flask import Flask, jsonify, render_template

from .data import ROWS, get_poll

app = Flask(__name__)


@app.template_filter("fmt_votes")
def fmt_votes(n: int) -> str:
    """Jinja2 filter that abbreviates a vote count for display (e.g. 1200 → '1.2K')."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


@app.route("/")
def index():
    """Render the main page with all poll rows.

    Builds a flat id→poll lookup dict so the template can embed the full
    poll payload as JSON for the client-side voting modal.
    """
    polls_by_id = {}
    for row in ROWS:
        for poll in row["polls"]:
            polls_by_id[poll["id"]] = poll
    total_polls = sum(len(row["polls"]) for row in ROWS)
    return render_template("index.html", rows=ROWS, polls_by_id=polls_by_id, total_polls=total_polls)


@app.route("/api/vote/<int:poll_id>/<int:option_idx>", methods=["POST"])
def vote(poll_id: int, option_idx: int):
    """Record a vote and return updated results.

    Increments the chosen option's count in memory, then returns the full
    results so the client can render animated progress bars without a page
    reload.

    Args:
        poll_id:    ID of the poll being voted on.
        option_idx: Zero-based index of the chosen option.

    Returns:
        JSON with keys:
          - ``total``   (int)  — new total vote count for the poll.
          - ``results`` (list) — each option as ``{text, votes, pct}``.

    Raises:
        404 if ``poll_id`` does not exist.
        400 if ``option_idx`` is out of range.
    """
    poll = get_poll(poll_id)
    if not poll:
        return jsonify({"error": "not found"}), 404
    if option_idx < 0 or option_idx >= len(poll["options"]):
        return jsonify({"error": "invalid option"}), 400

    poll["options"][option_idx]["votes"] += 1
    poll["total_votes"] += 1
    total = poll["total_votes"]

    return jsonify({
        "total": total,
        "results": [
            {
                "text": o["text"],
                "votes": o["votes"],
                "pct": round(o["votes"] / total * 100),
            }
            for o in poll["options"]
        ],
    })


def main():
    """Entry point for the `pollai` console script defined in pyproject.toml."""
    app.run(debug=True, port=5000)
