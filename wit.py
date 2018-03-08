#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import codecs
import sys
import requests
import json
import pyaudio
import wave
reload(sys)
sys.setdefaultencoding('utf8')

def read_audio(WAVE_FILENAME):
    # function to read audio(wav) file
    with open(WAVE_FILENAME, 'rb') as f:
        audio = f.read()
    return audio

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
 
# Wit.ai api access token
wit_access_token = 'KI4VRKXKS3RIZGCXPMCG64HTLT5VE3QP'
 
def ReconocimientoVoz(AUDIO_FILENAME):
 
    # record audio of specified length in specified audio file
 
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
 
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}
 
    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
 
    # converting response content to JSON format
    data = json.loads(resp.content)
 
    # get text from data
    text = data['_text']
 
    # return the text
    return text
 
if __name__ == "__main__":
    text =  ReconocimientoVoz('voz.wav')
    print("{}".format(text))
