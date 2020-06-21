# -*- coding: utf-8 -*-

import json
import azure.cognitiveservices.speech as speechsdk

def transcribe_azure(audio_path, azure_key, region, lang):
    '''
    Use Azure Speech-To-Text service. You can access the key from the following website.
    https://docs.microsoft.com/zh-tw/azure/cognitive-services/speech-service/get-started
    '''
    
    speech_config = speechsdk.SpeechConfig(subscription=azure_key, region=region, speech_recognition_language=lang)
    speech_config.request_word_level_timestamps()
    
    audio_config = speechsdk.audio.AudioConfig(filename=audio_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_recognizer.recognize_once()
    
    full_str = ''
    word_dict = []
    
    if result.text != '':
        stt = json.loads(result.json)
        confidences_in_nbest = [item['Confidence'] for item in stt['NBest']]
        best_index = confidences_in_nbest.index(max(confidences_in_nbest))
        words = stt['NBest'][best_index]['Words']
        for word in words:
            full_str = full_str + word['Word']
            word_dict.append({'word': word['Word'], 'from': word['Offset']*1e-7, 'to': (word['Offset']+word['Duration'])*1e-7})
    
    return full_str, word_dict


'''
免費試用
https://azure.microsoft.com/zh-tw/try/cognitive-services/

語言種類
https://docs.microsoft.com/zh-tw/azure/cognitive-services/speech-service/language-support

中文 zh-TW
英文 en-us
'''

azure_key = ''
region = ''

full_str, words = transcribe_azure('../audio/hello1.wav', azure_key, region, 'zh-TW')
print(full_str)





