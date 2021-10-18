# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify,redirect
from sqlalchemy import  text
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.serializer import Serializer
from common.libs.UserService import UserService
import requests

movie_page_Imdb = Blueprint( "movie_page_Imdb",__name__ )

@movie_page_Imdb.route("/movieImdbReviews")
def review():
    import json
    from jsonpath import jsonpath

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    #exampleMovieId = 'tt1375666'

    response = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + movieId)
    #reviews = jsonpath(response.json(),'$..items')

    movieReviewsDictionary = {
        "reviews": response.json()
    }
    
    return ops_renderJSON(msg = "Show Comments Successfull!", data = movieReviewsDictionary)
    

@movie_page_Imdb.route("/movieImdbInfo")
def Info():
    import json
    from jsonpath import jsonpath

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

    return ops_renderJSON(msg = "Show Comments Successfull!", data = movieInfoDictionary)


@movie_page_Imdb.route("/movieImdbBottom10Info")
def bottom():
    import json
    from jsonpath import jsonpath
    from bs4 import BeautifulSoup
    import requests
    import re
 
    # Getting imdb top 250 movie's data
    #url = 'http://www.imdb.com/chart/top'
    url = 'https://www.imdb.com/chart/bottom'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
 
    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
 
    ratings = [b.attrs.get('data-value')
                for b in soup.select('td.posterColumn span[name=ir]')]
 
    votes = [b.attrs.get('data-value')
                for b in soup.select('td.ratingColumn strong')]
 
    list = []
 
    # Create a empty list for storing movie information.
    list = []
 
    # Iterating over movies to extract each movie's details
    for index in range(0, 10):
     
        # Separating movie into: 'place', title', 'year'
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index))-(len(movie))]
        test = links[index]
        theMovieId = test[7:16]
        response3 = requests.get('https://imdb-api.com/en/API/Ratings/k_ds7a1ynu/' + theMovieId)
        rating = jsonpath(response3.json(),'$..imDb')
        response5 = requests.get('https://imdb-api.com/API/Posters/k_ds7a1ynu/' + theMovieId)
        posters = jsonpath(response5.json(),'$..posters')
        
        data = {"movie_title": movie_title,
                "Imdb_Rating": rating,
                "Imdb_Id": theMovieId,
                "posters": posters,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "vote": votes[index],
                "link": links[index]}
        list.append(data)
 
    # printing movie details with its rating.
    for movie in list:
        print(movie['place'], '-', movie['movie_title'], '('+movie['year'] + ') -', 'Starring:', movie['star_cast'], movie['rating'])
    


    
    return ops_renderJSON(msg = "Show Comments Successfull!", data = list)