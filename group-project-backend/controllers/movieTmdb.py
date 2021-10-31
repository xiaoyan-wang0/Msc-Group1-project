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
import json
from jsonpath import jsonpath
from common.libs.ToxicComments import do_pe,detector


movie_page_Tmdb = Blueprint( "movie_page_Tmdb",__name__ )

@movie_page_Tmdb.route("/movieTmdbReviews")
def review():
'''
    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
'''
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

    for review in reviews[0]:
        content = [review['content']]
        result = detector(content)
        review['toxic'] = result

    movieInfoDictionary = {
        "reviews": reviews
    }


    return ops_renderJSON(msg = "Show Successfull!", data = movieInfoDictionary)

@movie_page_Tmdb.route("/movieTmdbInfo")
def Info():
'''
    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
'''
  # I am using a Python Library for the TMDB API which is very convinient and easy to use.
    tmdb = TMDb()
    tmdb.language = 'en'
    tmdb.debug = True
    tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
    movie = Movie()

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    theId = str(movieId)

    # examplemovieId = 580489

    response2 = requests.get('https://api.themoviedb.org/3/movie/' + theId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
    genres = jsonpath(response2.json(),'$..genres')

    response3 = requests.get('https://api.themoviedb.org/3/movie/' + theId + '/credits?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
    cast = jsonpath(response3.json(),'$..cast')

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


