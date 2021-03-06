# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify
import requests
from sqlalchemy import  text
from application import db
from common.models.user import User
from common.models.userInfo2 import Userinfo2
from common.models.final import Final
from common.models.serializer import Serializer
from common.libs.ToxicComments import do_pe,detector
from common.libs.Sentiment import sentiment
from common.models.recommandation import Recommandation
from common.models.rec import Rec
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
import random

rec_page = Blueprint( "rec_page",__name__ )

'''
get recommendation by a specific movie

movieId
''' 
@rec_page.route("/getRecommendationById")
def getRecommadationById():

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    #check cache
    type = str(1)
    textsql = " 1=1 and movieId = '"+str(movieId)+"' and type = "+ type
    result = Rec.query.filter(text(textsql)).order_by(Rec.id.desc()).limit(1).first()
    if  result:
        return ops_renderJSON( msg = "get recommendation successfully!",data = result.content)


    movieId = int(movieId)
    number = 16

    #check dataset
    movie = Final.query.filter_by( movieId = movieId ).first()
    if movie is None:
        return ops_renderErrJSON( msg ="movie doesn't find")

    #call recommendation method
    list = getRecomendation(movieId, number)

    #save to cache
    model_rec = Rec()
    model_rec.content = list
    model_rec.movieId = movieId
    model_rec.type = 1
    db.session.add( model_rec )
    db.session.commit()
    db.session.close()
    db.engine.dispose()

    return ops_renderJSON( msg = "get recommendation successfully!",data = list)

'''
get recommendation by comments numbers

''' 
@rec_page.route("/getMostComments")
def getMostComments():
    
    #select database
    sql = 'SELECT movieId FROM usercomments GROUP BY movieId ORDER BY SUM(1) DESC LIMIT 3'
    result = db.session.execute(text(sql)).fetchall()

    list = []
    # call TMDb API
    for lis in result:
        movieInfoDictionary = getTmdbInfo(lis[0], lis[0])
        list.append(movieInfoDictionary)
    db.session.close()
    db.engine.dispose()

    return ops_renderJSON( msg = "get most comments successfully!",data = list)

'''
set movie history 

movieId
userId
tagId
''' 
@rec_page.route("/setRecommandation")
def setRecommandation():
    
    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""
    userId = req['userId'] if "userId" in req else ""
    tagId = req['tagId'] if "tagId" in req else ""

    if userId != "":
        user = User.query.filter_by( userId = userId ).first()
        #check if user exist
        if user:
            #save history record
            model_rec = Recommandation()
            model_rec.movieId = movieId
            model_rec.userId = userId
            model_rec.tagId = tagId
            db.session.add( model_rec )
            db.session.commit()
            db.session.close()
            db.engine.dispose()
    
    return ops_renderJSON( msg = "set recommandation successfully!")

'''
show movie history recently 5

userId
''' 
@rec_page.route("/showHistory")
def showHistory():
    
    req = request.values
    userId = req['userId'] if "userId" in req else ""

    if userId !="":
        sql = 'SELECT a.movieId,a.id FROM(select movieId, MAX(id) as id from recommandation WHERE userId = ' + userId +' group by movieId) a  order by a.id desc limit 5;'
        result = db.session.execute(text(sql)).fetchall()

        #call TMDb to get movie Infomation
        movieList = []
        for lis in result:
            movieInfoDictionary = getTmdbInfo(str(lis[0]), lis[0])
            if movieInfoDictionary:
                movieList.append(movieInfoDictionary)
                
    db.session.close()
    db.engine.dispose()

    return ops_renderJSON( msg = "show history successfully!",data = movieList)

'''
get recommandation based on recently history records

userId
''' 
@rec_page.route("/getRecommandation")
def getRecommandation():

    req = request.values
    userId = req['userId'] if "userId" in req else ""

    if userId !="":
        sql = 'SELECT tagId,id,movieId FROM recommandation WHERE id IN (select MAX(id) AS id from recommandation WHERE userId = ' + userId +'  group by movieId) order by id desc limit 5;'
        result = db.session.execute(text(sql)).fetchall()

        num_to_label = {
        '28':'Action',
        '12':'Adventure',
        '16':'Animation',
        '35':'Comedy',
        '80':'Crime',
        '99':'Documentary',
        '18':'Drama',
        '10751':'Family',
        '14':'Fantasy',
        '36':'History',
        '27':'Horror',
        '10402':'Music',
        '9648':'Mystery',
        '10749':'Romance',
        '878':'Science Fiction',
        '10770':'TV Movie',
        '53':'Thriller',
        '10752':'War',
        '37':'Western'
        }

        movie = []

        #recommendation by tag
        if result:
            for lis in result:             
                tagName = num_to_label[str(lis[0])]
                movies = getTagMovies(tagName, 8)
                taglist = movies.to_dict('list')['id']
                movie.extend(taglist)
        movie=list(set(movie))

        movieList = []
        for lis in movie:
            movieInfoDictionary = getTmdbInfo(str(lis), lis)
            if movieInfoDictionary:
                movieList.append(movieInfoDictionary)

    db.session.close()
    db.engine.dispose()

    return ops_renderJSON( msg = "get recommandation successfully!",data = movieList)

'''
get recommandation by tags user set

userId
''' 
@rec_page.route("/getRecommandationByTags")
def getRecommandationByTags():

    req = request.values
    userId = req['userId'] if "userId" in req else ""
    userInfo = Userinfo2.query.filter_by( userId = userId ).first()

    #check cache
    type = str(3)
    textsql = " 1=1 and userId = '"+str(userId)+"' and type = "+ type 
    result = Rec.query.filter(text(textsql)).order_by(Rec.id.desc()).limit(1).first()
    if  result:
        return ops_renderJSON( msg = "get recommendation successfully!",data = result.content)


    num_to_label = {
    '28':'Action',
    '12':'Adventure',
    '16':'Animation',
    '35':'Comedy',
    '80':'Crime',
    '99':'Documentary',
    '18':'Drama',
    '10751':'Family',
    '14':'Fantasy',
    '36':'History',
    '27':'Horror',
    '10402':'Music',
    '9648':'Mystery',
    '10749':'Romance',
    '878':'Science Fiction',
    '10770':'TV Movie',
    '53':'Thriller',
    '10752':'War',
    '37':'Western'
    }
    movie = []
    # recommendate by tag
    if userInfo:
        tag = userInfo.movieTags
        #tag = "28,99,37"
        if tag != "":
            if tag:
                mlist = tag.split(",")
                tuple(mlist)
                if len(mlist) > 3:
                    number = 3
                else:
                    number = 6
                for lis in mlist:
                        tagName = num_to_label[lis]
                        movies = getTagMovies(tagName, number)
                        taglist = movies.to_dict('list')['id']
                        movie.extend(taglist)
    movie=list(set(movie))

    movieList = []
    for lis in movie:
        movieInfoDictionary = getTmdbInfo(str(lis), lis)
        if movieInfoDictionary:
            movieList.append(movieInfoDictionary)


    #cache saving
    model_rec = Rec()
    model_rec.content = movieList
    model_rec.userId = userId
    model_rec.type = 3
    db.session.add( model_rec )
    db.session.commit()
    db.session.close()
    db.engine.dispose()

    
    return ops_renderJSON( msg = "get recommandation successfully!",data = movieList)

'''
get recommandation by tags 
core method

tagName
number
''' 
def getTagMovies(tagName, number):
    import pandas as pd
    from pandas import DataFrame,Series
    import json
    import csv
    from tqdm.notebook import tqdm

    dx=pd.read_csv("~/Msc-Group1-project/group-project-backend/database/profile_movie.csv")

    movies=dx.loc[(dx['label'] == tagName) & (dx['popularity']>100)].head(number)
    return movies


'''
get recommandation - cotent based
core method

movieId
number - how many movie to recommend
''' 
def getRecomendation(movieId, number):
    #train_movies_1 = pd.read_csv('C:/final.csv')
    #path on ubuntu(AWS)
    train_movies_1 = pd.read_csv('~/Msc-Group1-project/group-project-backend/database/final.csv')

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

    dic = train_movies_1["id"].iloc[sim_index]
    list = []

    for k in dic:
        theId = str(k)
        movieId = int(theId)
        # I am using a Python Library for the TMDB API which is very convinient and easy to use.
        movieInfoDictionary = getTmdbInfo(theId, movieId)
        if movieInfoDictionary:
            list.append(movieInfoDictionary)
            
    return list

'''
get TMDb Information
core method

theId
movieId
''' 
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
    try:
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
        id = m.id
        backdrop_path = m.backdrop_path
        title = m.title
        overview = m.overview
        poster = m.poster_path
        vote_average = m.vote_average
        year = m.release_date
        runtime = m.runtime
        popularity = m.popularity

        movieInfoDictionary = {
            "id": id,
            "backdrop_path": backdrop_path,
            "title": title,
            "genres": genres,
            "overview": overview,
            "imdb_Id": imdb_id,
            "release_date": year,
            "poster": poster,
            "vote_average": vote_average,
            "runtime": runtime,
            "popularity": popularity,
        }
    
    except Exception:
        return

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

