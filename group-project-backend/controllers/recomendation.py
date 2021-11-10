# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify
import requests
from sqlalchemy import  text
from application import db
from common.models.user import User
from common.models.serializer import Serializer
from common.libs.ToxicComments import do_pe,detector
from common.libs.Sentiment import sentiment
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
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
from tmdbv3api import TMDb
from tmdbv3api import Movie
from requests_futures.sessions import FuturesSession

rec_page = Blueprint( "rec_page",__name__ )

@rec_page.route("/getRecommadationById")
def getRecommadationById():
    # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""
    movieId = int(movieId)
    number = 6

    list = getRecomendation(movieId, number)

    return ops_renderJSON( msg = "delete movieLikes successfully!",data = list)

def getRecomendation(movieId, number):
    train_movies_1 = pd.read_csv('C:/final.csv')
    #print(type(train_movies_1))
    train_movies_1.dtypes
    train_movies_1.isnull().sum(axis=0)
    train_movies_1.dropna()
    train_movies_1.drop(["Unnamed: 0","Unnamed: 0.1",'genre_ids'], axis = 1,inplace = True)
    #train_movies_1
    train_movies_1=train_movies_1.drop_duplicates()
    #train_movies_1
    train_movies_1=train_movies_1.reset_index(drop=True)
    #train_movies_1
    tf=TfidfVectorizer(stop_words="english")
    tf_matrix= tf.fit_transform(train_movies_1['overview'])
    consine_sim= pairwise_kernels(tf_matrix,tf_matrix)
    indeces= pd.Series(train_movies_1.index, index=train_movies_1["id"])

    id = movieId

    idx= indeces[movieId]
    sim_score= enumerate(consine_sim[idx])
    sim_score= sorted (sim_score, key=lambda x: x[1], reverse= True)
    sim_score=sim_score[1:number]
    sim_index=[i[0] for i in sim_score]
    print(train_movies_1["id"].iloc[sim_index])
    print(type(train_movies_1["id"].iloc[sim_index]))

    dic = train_movies_1["id"].iloc[sim_index]
    list = []

    for k in dic:
        theId = str(k)

        # I am using a Python Library for the TMDB API which is very convinient and easy to use.
        movieInfoDictionary = getTmdbInfo(theId, movieId)
        list.append(movieInfoDictionary)
    return list

def getTmdbInfo(theId, movieId):
    # I am using a Python Library for the TMDB API which is very convinient and easy to use.
    tmdb = TMDb()
    tmdb.language = 'en'
    tmdb.debug = True
    tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
    movie = Movie()

    # examplemovieId = 580489

    urls = [
        'https://api.themoviedb.org/3/movie/' + theId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1',
        'https://api.themoviedb.org/3/movie/' + theId + '/credits?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1'
    ]

    counter = 0
    with FuturesSession() as session:
        futures = [session.get(url) for url in urls]
        for future in futures:
            if counter == 0:
                genres = jsonpath(future.result().json(),'$..genres')
            # elif counter == 1:
            #     cast = jsonpath(future.result().json(),'$..cast')
            counter = counter + 1

    m = movie.details(movieId)
    imdb_id = m.imdb_id
    title = m.title
    overview = m.overview
    poster = m.poster_path
    vote_average = m.vote_average
    year = m.release_date
    runtime = m.runtime
    popularity = m.popularity

    movieInfoDictionary = {
        "title": title,
        "genres": genres,
        "overview": overview,
        "imdb Id": imdb_id,
        "release date": year,
        "poster": poster,
        "vote average": vote_average,
        "runtime": runtime,
        "popularity": popularity,
    }
    return movieInfoDictionary

# def get_recomendation(indeces, id, consine_sim, train_movies_1):
#     idx= indeces[id]
#     sim_score= enumerate(consine_sim[idx])
#     sim_score= sorted (sim_score, key=lambda x: x[1], reverse= True)
#     sim_score=sim_score[1:5]
#     sim_index=[i[0] for i in sim_score]
#     print(train_movies_1["id"].iloc[sim_index])
#     print(type(train_movies_1["id"].iloc[sim_index]))

#     dic = train_movies_1["id"].iloc[sim_index]
#     lis = []
#     for value  in train_movies_1["id"].iloc[sim_index]:
#         print(value)

