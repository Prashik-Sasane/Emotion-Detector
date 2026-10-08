# Emotion Detector

Emotion Detector is a simple Flask application that analyzes text and predicts the dominant emotion using IBM Watson NLP Emotion Analysis.

## Overview

This project demonstrates how to send text to the Watson NLP Emotion Analysis service and interpret the emotion scores for:

- anger
- disgust
- fear
- joy
- sadness

The application identifies the dominant emotion and presents the results through a simple web interface.

## Technologies Used

- Python 3
- Flask
- Requests
- IBM Watson NLP
- unittest
- Pylint
- HTML
- JavaScript

## Features

- Text input form for emotion detection
- Analysis of five emotion categories
- Displays emotion scores
- Identifies the dominant emotion
- Handles blank input
- Handles invalid/error responses
- Unit tests for emotion detection
- Flask web deployment
- Simple and beginner-friendly project structure

## Project Structure

```text
oaqjp-final-project-emb-ai/
├── README.md
├── requirements.txt
├── server.py
├── test_emotion_detection.py
├── .gitignore
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
└── templates/
    └── index.html