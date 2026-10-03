"""Emotion detection using Watson NLP."""

import os

import requests


EMPTY_RESPONSE = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}


def emotion_detector(text_to_analyze):
    """Analyze text with the Watson NLP emotion service and return results."""
    if text_to_analyze is None or not str(text_to_analyze).strip():
        return dict(EMPTY_RESPONSE)

    api_key = os.getenv("WATSON_API_KEY", "test-api-key")
    instance_id = os.getenv("WATSON_INSTANCE_ID", "test-instance")
    service_url = os.getenv(
        "WATSON_URL",
        "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com",
    )
    version = os.getenv("WATSON_VERSION", "2022-04-07")

    url = f"{service_url}/instances/{instance_id}/v1/analyze?version={version}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "text": str(text_to_analyze),
        "features": {"emotion": {}},
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
    except requests.RequestException:
        return dict(EMPTY_RESPONSE)

    if response.status_code == 400 or response.status_code >= 400:
        return dict(EMPTY_RESPONSE)

    try:
        data = response.json()
    except ValueError:
        return dict(EMPTY_RESPONSE)

    try:
        emotion_data = data["emotion"]["document"]["emotion"]
    except (KeyError, TypeError, IndexError):
        return dict(EMPTY_RESPONSE)

    result = {
        "anger": float(emotion_data.get("anger", 0.0) or 0.0),
        "disgust": float(emotion_data.get("disgust", 0.0) or 0.0),
        "fear": float(emotion_data.get("fear", 0.0) or 0.0),
        "joy": float(emotion_data.get("joy", 0.0) or 0.0),
        "sadness": float(emotion_data.get("sadness", 0.0) or 0.0),
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result
