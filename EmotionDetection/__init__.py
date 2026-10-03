"""Flask application for emotion detection."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Render the main page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """Handle text submitted by the user and return detected emotions."""
    if request.is_json:
        payload = request.get_json(silent=True) or {}
        text_to_analyze = str(payload.get("text", "") or "")
    else:
        text_to_analyze = request.form.get("text", "")

    text_to_analyze = text_to_analyze.strip()

    if not text_to_analyze:
        error_message = "Please enter a valid text."
        if request.is_json:
            return jsonify({"error": error_message}), 400
        return render_template("index.html", error=error_message)

    results = emotion_detector(text_to_analyze)

    if request.is_json:
        return jsonify(results)

    return render_template("index.html", text=text_to_analyze, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
