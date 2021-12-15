# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify,redirect,g
from sqlalchemy import  text
from sqlalchemy.sql.expression import over
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.serializer import Serializer
from common.libs.UserService import UserService
import requests
from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests
from common.models.reviews import Review
from common.models.recommandation import Recommandation
import json
from jsonpath import jsonpath
from common.libs.ToxicComments import do_pe,detector
from common.libs.Sentiment import sentiment
from requests_futures.sessions import FuturesSession


movie_page_Tmdb = Blueprint( "movie_page_Tmdb",__name__ )

'''
show Comments from TMDb

movieId
'''   
@movie_page_Tmdb.route("/movieTmdbReviews")
def review():

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    #check cache
    type = str(2)
    textsql = " 1=1 and movieId = "+movieId+" and type = "+ type
    result = Review.query.filter(text(textsql)).order_by(Review.reviewId.desc()).limit(1).first()
    if  result:
        return ops_renderJSON(msg = "Show Successfull!", data = result.content)


    # I am using a Python Library for the TMDB API which is very convinient and easy to use.
    tmdb = TMDb()
    tmdb.language = 'en'
    tmdb.debug = True
    tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
    movie = Movie()

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    theId = str(movieId)

    response = requests.get('https://api.themoviedb.org/3/movie/' + theId + '/reviews?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
    reviews = jsonpath(response.json(),'$..results')
    
    #call detector
    for review in reviews[0]:
        content = [review['content']]
        result = detector(content)
        senti = sentiment(content)
        review['toxic'] = result['tag']
        review['sentiment'] = senti['tag']

    movieInfoDictionary = {
        "reviews": reviews
    }

    #save to cache
    model_reviews = Review()
    model_reviews.content = movieInfoDictionary
    model_reviews.movieId = movieId
    model_reviews.type = 2
    db.session.add( model_reviews )
    db.session.commit()
    db.session.close()
    db.engine.dispose()

    return ops_renderJSON(msg = "Show Successfull!", data = movieInfoDictionary)

'''
show movie Information details

movieId
userId
''' 
@movie_page_Tmdb.route("/movieTmdbInfo")
def Info():

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""
    userId = req['userId'] if "userId" in req else ""

    #save history
    if userId != "":
        user = User.query.filter_by( userId = userId ).first()
        if user:
            model_rec = Recommandation()
            model_rec.movieId = movieId
            model_rec.userId = userId
            db.session.add( model_rec )
            db.session.commit()
            db.session.close()
            db.engine.dispose()


    # I am using a Python Library for the TMDB API which is very convinient and easy to use.
    tmdb = TMDb()
    tmdb.language = 'en'
    tmdb.debug = True
    tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
    movie = Movie()

    theId = str(movieId)

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
            elif counter == 1:
                cast = jsonpath(future.result().json(),'$..cast')
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
        "cast": cast,
        "popularity": popularity,
    }

        
    return ops_renderJSON(msg = "Show Successfull!", data = movieInfoDictionary)