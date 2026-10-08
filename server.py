from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main emotion detector page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the emotion of the text submitted by the user."""
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle blank or empty input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)