import requests
import json
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=Headers)
    
    #extract required format
    output = json.loads(response.text)
    anger_score = output['emotionPredictions'][0]['emotion']['anger']
    dominant_emotion_score = anger_score
    domiant_emotion = 'anger'
    disgust_score = output['emotionPredictions'][0]['emotion']['disgust']
    if dominant_emotion_score < disgust_score:
        dominant_emotion_score = disgust_score
        domiant_emotion = 'disgust'
    fear_score = output['emotionPredictions'][0]['emotion']['fear']
    if dominant_emotion_score < fear_score:
        dominant_emotion_score = fear_score
        domiant_emotion = 'fear'
    joy_score = output['emotionPredictions'][0]['emotion']['joy']
    if dominant_emotion_score < joy_score:
        dominant_emotion_score = joy_score
        domiant_emotion = 'joy'
    sadness_score = output['emotionPredictions'][0]['emotion']['sadness']
    if dominant_emotion_score < sadness_score:
        dominant_emotion_score = sadness_score
        domiant_emotion = 'sadness'
    #return dictionary output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': domiant_emotion
    }

    