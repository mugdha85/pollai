from flask import Flask, jsonify, render_template

from .data import ROWS, get_poll

app = Flask(__name__)


@app.template_filter("fmt_votes")
def fmt_votes(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


@app.route("/")
def index():
    polls_by_id = {}
    for row in ROWS:
        for poll in row["polls"]:
            polls_by_id[poll["id"]] = poll
    total_polls = sum(len(row["polls"]) for row in ROWS)
    return render_template("index.html", rows=ROWS, polls_by_id=polls_by_id, total_polls=total_polls)


@app.route("/api/vote/<int:poll_id>/<int:option_idx>", methods=["POST"])
def vote(poll_id: int, option_idx: int):
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
    app.run(debug=True, port=5000)
