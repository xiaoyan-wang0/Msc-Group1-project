# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify,redirect,g
from sqlalchemy import  text
from sqlalchemy.sql.expression import null
from tmdbv3api import tmdb
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.serializer import Serializer
from common.libs.UserService import UserService
import requests
from common.libs.ToxicComments import do_pe,detector
from common.libs.Sentiment import sentiment
from requests_futures.sessions import FuturesSession
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import pairwise_kernels
from jsonpath import jsonpath


movie_page_Recommandation = Blueprint( "movie_page_Recomanndation",__name__ )

@movie_page_Recommandation.route("/movieRecommandationInfo")
def recommandation():
    train_movies_1 = pd.read_csv('/Users/egebilir/Desktop/Project/final.csv')

    type(train_movies_1)

    train_movies_1.dtypes

    train_movies_1.isnull().sum(axis=0)

    train_movies_1.dropna()

    train_movies_1.drop(["Unnamed: 0","Unnamed: 0.1",'genre_ids'], axis = 1,inplace = True)

    train_movies_1

    train_movies_1=train_movies_1.drop_duplicates()

    train_movies_1

    train_movies_1=train_movies_1.reset_index(drop = True)

    train_movies_1

    train_movies_1.loc[(train_movies_1['id'] == 639721)]

    train_movies_1.loc[(train_movies_1['id'] == 11508)]

    tf = TfidfVectorizer(stop_words="english")
    tf_matrix = tf.fit_transform(train_movies_1['overview'])

    consine_sim = pairwise_kernels(tf_matrix,tf_matrix)
    indeces= pd.Series(train_movies_1.index, index=train_movies_1["id"])

    indeces

    idx = indeces[774021]

    idx

    def get_recomendation(id, semilar= consine_sim):
        idx = indeces[id]
        sim_score = enumerate(consine_sim[idx])
        sim_score = sorted (sim_score, key=lambda x: x[1], reverse= True)
        sim_score = sim_score[1:10]
        sim_index=[i[0] for i in sim_score]
        output = []
        for item in train_movies_1["id"].iloc[sim_index]:
            output.append(item)
        return  output

    result = get_recomendation(639721)

    list = []

    for k in result:
        theId = str(k)
        response = requests.get('https://api.themoviedb.org/3/movie/' + theId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
        title = jsonpath(response.json(),'$.belongs_to_collection..name')
        list.append(title)

    return ops_renderJSON(msg = "Show Comments Successfull!", data = list)