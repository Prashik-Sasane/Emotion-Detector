# Emotion Detector

Emotion Detector is a simple Flask application that analyzes text and predicts the dominant emotion using IBM Watson NLP Emotion Analysis.

## Overview

This project demonstrates how to send text to the Watson Natural Language Understanding (NLU) Emotion Analysis API and interpret the emotion scores for:

- anger
- disgust
- fear
- joy
- sadness

The app identifies the dominant emotion and presents the results in a clean web interface.

## Technologies Used

- Python 3
- Flask
- Requests
- IBM Watson NLP / NLU
- unittest
- Pylint

## Features

- Text input form for emotion detection
- Analysis of five emotion categories
- Displays the dominant emotion
- Graceful handling for blank or invalid input
- Beginner-friendly code structure
- Unit tests for validation

## Project Structure

```text
Emotion-Detector/
├── README.md
├── requirements.txt
├── server.py
├── test_emotion_detection.py
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
└── templates/
    └── index.html
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Prashik-Sasane/Emotion-Detector.git
cd Emotion-Detector
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask app:

```bash
python server.py
```

Then open this URL in your browser:

```text
http://127.0.0.1:5000
```

## Run Unit Tests

```bash
python -m unittest discover -v
```

## Run Pylint

```bash
pylint server.py
pylint EmotionDetection/emotion_detection.py
```

## Watson NLP Setup

Set the required environment variables before running the application:

```bash
export WATSON_API_KEY="your_api_key"
export WATSON_INSTANCE_ID="your_instance_id"
export WATSON_URL="https://api.us-south.natural-language-understanding.watson.cloud.ibm.com"
export WATSON_VERSION="2022-04-07"
```

If the values are missing or the service is unavailable, the app returns a safe empty/error result instead of crashing.

## Contributing

If you want to contribute:

```bash
git checkout -b feature/your-change
git status
git add .
git commit -m "Add your change"
git push origin feature/your-change
```

Then open a pull request in GitHub.

## Notes

This project is intentionally kept simple and beginner-friendly so it can be used for learning, demos, and automated evaluation.
