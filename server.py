from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.get("/")
def home():
    return render_template('index.html')


@app.get("/emotionDetector")
def emotion_detection():
    textToAnalyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(textToAnalyze)
    return f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}"
