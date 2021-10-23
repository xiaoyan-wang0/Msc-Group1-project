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
model_path = '/root/flask_vue_ML'




expose = Flask(__name__)
expose.secret_key = "super_secret_key"



@expose.route('/', methods=['GET'])
def index():
    return jsonify("DL API")


@expose.route('/api/tasks', methods=['GET'])
def get_result():
    result = []
    try:
        data_result = session['my_result']
        result.append ({'title': data_result['title'], 'tag': data_result['tag'] })
    except:
        result.append ({'title': 'The txt you input', 'tag': 'Percentage' })
    return jsonify(result)

@expose.route('/api/task', methods=['POST','GET'])
def input_predict_text():


    title = [request.get_json()['title']]


    input_data_json = json.dumps({"signature_name": "serving_default",
                   "instances": title})

    headers = {"content-type": "application/json"}          
    
    response = requests.post('http://localhost:8501/v1/models/mymodel2:predict', data=input_data_json,headers=headers)
  
 
    
    text1 =  title

    label =  json.loads(response.text)['predictions'][0]

    
   


    result = {'title' : text1, 'tag' :  label}
    session['my_result'] = result
    
    return jsonify(result)

if __name__ == '__main__':

    with open('tokenizer_4.pickle', 'rb') as f:
         tokenizer = pickle.load(f)

   ## with open('tokenizer.json') as f:
   ##      data = json_load(f)
   ##      tokenizer_obj = tokenizer_from_json(data)
    

    expose.run(debug=True)
   
