from json import load as json_load
import json
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import pickle
import requests
import numpy as np


def do_pe(rs):
    pr=[]
    for r in rs:
        r = r.lower()
        pr.append(re.sub('[^a-zA-z0-9\s]','',r))



    return pr

#call docker model
def detector(title):
    data = do_pe(title)

    input_data_json = json.dumps({"signature_name": "serving_default",
                                        "instances": data})

    headers = {"content-type": "application/json"}          

    #response = requests.post('http://0.0.0.0:8501/v1/models/mymodel:predict', data=input_data_json,headers=headers)
    #response = requests.post('http://localhost:8501/v1/models/mymodel:predict', data=input_data_json,headers=headers)
    response = requests.post('http://172.26.4.154:8501/v1/models/mymodel:predict', data=input_data_json,headers=headers)

    text1 =  title

    label =  json.loads(response.text)['predictions']
    result = {'title' : text1, 'tag' : label}
    return result