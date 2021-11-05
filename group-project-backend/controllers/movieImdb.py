# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify,redirect,g
from sqlalchemy import  text
from sqlalchemy.sql.expression import null
from tmdbv3api import tmdb
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.reviews import Review
from common.models.serializer import Serializer
from common.libs.UserService import UserService
import requests
from common.libs.ToxicComments import do_pe,detector
from common.libs.Sentiment import sentiment


movie_page_Imdb = Blueprint( "movie_page_Imdb",__name__ )

@movie_page_Imdb.route("/movieImdbReviews")
def review():
    import json
    from jsonpath import jsonpath
    
    '''
    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
    ''' 
    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""
    type = str(2)
    textsql = " 1=1 and movieId = '"+movieId+"' and type = "+ type
    result = Review.query.filter(text(textsql)).order_by(Review.reviewId.desc()).limit(1).first()
    if  result:
        return ops_renderJSON(msg = "Show Successfull!", data = result.content)



    exampleMovieId = 'tt1375666'

    response = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + movieId)
    #reviews = jsonpath(response.json(),'$..items')
    reviews = response.json()

    for review in reviews['items']:
        content = [review['content']]
        result = detector(content)
        senti = sentiment(content)
        review['toxic'] = result['tag']
        review['sentiment'] = senti['tag']

    movieReviewsDictionary = {
        "reviews": reviews
    }

    model_reviews = Review()
    model_reviews.content = movieReviewsDictionary
    model_reviews.movieId = movieId
    model_reviews.type = 2
    db.session.add( model_reviews )
    db.session.commit()
    
    return ops_renderJSON(msg = "Show Successfull!", data = movieReviewsDictionary)
    
@movie_page_Imdb.route("/movieImdbInfo")
def Info():
    import json
    from jsonpath import jsonpath
    '''
    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
    '''    
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

@movie_page_Imdb.route("/movieImdbBottomInfo")
def bottom():
    import json
    from jsonpath import jsonpath
    from bs4 import BeautifulSoup
    import requests
    import re

    req = request.values
    numberOfMovies = req['numberOfMovies'] 
 
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
    # Max has to br 100!!!,
    counter = 0
    for index in range(0, int(numberOfMovies)):
     
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

        response5 = requests.get('https://api.themoviedb.org/3/movie/' + theMovieId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
        posters = jsonpath(response5.json(),'$..poster_path')
        tmdbId = jsonpath(response5.json(),'$..id')
        genres = jsonpath(response5.json(),'$.genres..name')

        try:
           theTmdbId = tmdbId[0]
        except:
            theTmdbId = 0
            
        data = {"movie_title": movie_title,
                "Imdb_Rating": rating,
                "Imdb_Id": theMovieId,
                "tmdb_Id": theTmdbId,
                "posters": posters,
                "genres": genres,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "link": links[index]}
        list.append(data)
    
    return ops_renderJSON(msg = "Show Comments Successfull!", data = list)
