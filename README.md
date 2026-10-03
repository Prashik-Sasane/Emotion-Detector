<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emotion Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 40px 20px;
        }
        .container {
            max-width: 700px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
            padding: 30px;
        }
        h1 {
            text-align: center;
            color: #2d3748;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 10px;
        }
        textarea {
            width: 100%;
            min-height: 120px;
            padding: 12px;
            border: 1px solid #cbd5e0;
            border-radius: 8px;
            box-sizing: border-box;
            font-size: 16px;
        }
        button {
            margin-top: 15px;
            background: #2563eb;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        .error {
            color: #b91c1c;
            font-weight: bold;
            margin-top: 15px;
        }
        .results {
            margin-top: 25px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px 20px;
        }
        .results p {
            margin: 8px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Emotion Detector</h1>

        <form method="POST" action="/emotionDetector">
            <label for="text">Enter text:</label>
            <textarea id="text" name="text">{{ text or '' }}</textarea>
            <button type="submit">Analyze Emotion</button>
        </form>

        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}

        {% if results %}
            <div class="results">
                <p>Anger: {{ results.anger }}</p>
                <p>Disgust: {{ results.disgust }}</p>
                <p>Fear: {{ results.fear }}</p>
                <p>Joy: {{ results.joy }}</p>
                <p>Sadness: {{ results.sadness }}</p>
                <p>Dominant Emotion: {{ results.dominant_emotion }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
