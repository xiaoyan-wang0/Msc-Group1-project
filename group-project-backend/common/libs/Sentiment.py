from io import TextIOBase
from flask import Flask, jsonify, request
import numpy as np
import requests
from flask import session
import math
import pickle
import json
from json import load as json_load
import re
import tensorflow as tf
from requests.models import to_native_string
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json


def index():
    return jsonify("DL API")


def get_result():
    result = []
    try:
        data_result = session['my_result']
        result.append ({'title': data_result['title'], 'tag': data_result['tag'] })
    except:
        result.append ({'title': 'The txt you input', 'tag': 'Percentage' })
    return jsonify(result)

#call docker model
def sentiment(title):



    input_data_json = json.dumps({"signature_name": "serving_default",
                   "instances": title})

    headers = {"content-type": "application/json"}          
    
    #response = requests.post('http://0.0.0.0:8501/v1/models/mymodel2:predict', data=input_data_json,headers=headers)
    #response = requests.post('http://localhost:8501/v1/models/mymodel2:predict', data=input_data_json,headers=headers)
    response = requests.post('http://172.26.4.154:8501/v1/models/mymodel2:predict', data=input_data_json,headers=headers)
    text1 =  title

    label =  json.loads(response.text)['predictions']

    label = np.float64(np.argmax(label))

    # 'positive':1, 
    # 'negative':0,
    # 'neutral':2, 

    result = {'title' : text1, 'tag' :  label}
    
    return result