import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = data, headers = headers)
    response_data = json.loads(response.text)
    
    emotions_data = response_data["emotionPredictions"][0]["emotion"]
    
    max_name = ""
    max_score = None

    for name in emotions_data:
        score = emotions_data[name]
        
        if max_score == None or score > max_score:
            max_score = score
            max_name = name
    
    emotions_data["dominant_emotion"] = max_name

    return emotions_data

