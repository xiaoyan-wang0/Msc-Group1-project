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
    with open('./tokenizer_4.pickle', 'rb') as f:
        tokenizer = pickle.load(f)
    for r in rs:
        r = r.lower()
        pr.append(re.sub('[^a-zA-z0-9\s]','',r))

    pr = tokenizer.texts_to_sequences(np.array(pr))
    pr = pad_sequences(pr, maxlen=300)

    return pr


def detector(title):
    data = do_pe(title)

    input_data_json = json.dumps({"signature_name": "serving_default",
                                        "instances": data.tolist()})

    headers = {"content-type": "application/json"}          

    response = requests.post('http://0.0.0.0:8501/v1/models/mymodel:predict', data=input_data_json,headers=headers)
    #response = requests.post('http://localhost:8501/v1/models/mymodel:predict', data=input_data_json,headers=headers)
    #response = requests.post('http://172.26.9.231:8501/v1/models/mymodel:predict', data=input_data_json,headers=headers)

    text1 =  title

    label =  json.loads(response.text)['predictions'][0]
    result = {'title' : text1, 'tag' : label}
    return result