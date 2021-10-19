# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify,redirect,g
from sqlalchemy import  text
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.serializer import Serializer
from common.libs.UserService import UserService
import requests
from common.libs.ToxicComments import do_pe,detector


movie_page_Imdb = Blueprint( "movie_page_Imdb",__name__ )

@movie_page_Imdb.route("/movieImdbReviews")
def review():
    import json
    from jsonpath import jsonpath

    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    exampleMovieId = 'tt1375666'

    response = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + movieId)
    #reviews = jsonpath(response.json(),'$..items')
    reviews = response.json()

    for review in reviews['items']:
        content = [review['content']]
        result = detector(content)
        review['toxic'] = result

    movieReviewsDictionary = {
        "reviews": reviews
    }
    
    return ops_renderJSON(msg = "Show Successfull!", data = movieReviewsDictionary)
    
@movie_page_Imdb.route("/movieImdbInfo")
def Info():
    import json
    from jsonpath import jsonpath

    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
    
    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    exampleMovieId = 'tt1375666'

    response = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + movieId)
    title = jsonpath(response.json(),'$..fullTitle')
    type = jsonpath(response.json(),'$..type')
    year = jsonpath(response.json(),'$..year')

    response2 = requests.get('https://imdb-api.com/en/API/Title/k_ds7a1ynu/' + movieId)
    plot = jsonpath(response2.json(),'$..plot')

    response3 = requests.get('https://imdb-api.com/en/API/Ratings/k_ds7a1ynu/' + movieId)
    rating = jsonpath(response3.json(),'$..imDb')

    response4 = requests.get('https://imdb-api.com/en/API/FullCast/k_ds7a1ynu/' + movieId)
    cast = jsonpath(response4.json(),'$..actors')

    response5 = requests.get('https://imdb-api.com/API/Posters/k_ds7a1ynu/' + movieId)
    posters = jsonpath(response5.json(),'$..posters')
    
    # Eliminates empty plots
    plotFinal = ''
    for p in plot:
        if p != '':
            plotFinal = p
   

    #movieInfoDictionary[exampleMovieId] = title

    movieInfoDictionary = {
        "title": title,
        "year": year,
        "type": type,
        "plot": plotFinal,
        "cast (actors)": cast,
        "posters": posters,
        "Imdb Rating": rating
    }

    return ops_renderJSON(msg = "Show Successfull!", data = movieInfoDictionary)