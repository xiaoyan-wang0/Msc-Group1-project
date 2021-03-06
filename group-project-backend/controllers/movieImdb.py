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
from requests_futures.sessions import FuturesSession
import json
from jsonpath import jsonpath
from bs4 import BeautifulSoup
import requests
import re


movie_page_Imdb = Blueprint( "movie_page_Imdb",__name__ )

'''
show Comments from IMDb

movieId
'''
@movie_page_Imdb.route("/movieImdbReviews")
def review():
    import json
    from jsonpath import jsonpath
    
    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    #check cache
    type = str(1)
    textsql = " 1=1 and movieId = '"+str(movieId)+"' and type = "+ type
    result = Review.query.filter(text(textsql)).order_by(Review.reviewId.desc()).limit(1).first()
    if  result:
        return ops_renderJSON(msg = "Show Successfull!", data = result.content)

    exampleMovieId = 'tt1375666'

    #call api
    response = requests.get('https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + movieId)
    reviews = response.json()

    #call detector
    for review in reviews['items']:
        content = [review['content']]
        result = detector(content)
        senti = sentiment(content)
        review['toxic'] = result['tag']
        review['sentiment'] = senti['tag']

    movieReviewsDictionary = {
        "reviews": reviews
    }

    #save to cache
    model_reviews = Review()
    model_reviews.content = movieReviewsDictionary
    model_reviews.movieId = movieId
    model_reviews.type = 1
    db.session.add( model_reviews )
    db.session.commit()
    db.session.close()
    db.engine.dispose()
    
    return ops_renderJSON(msg = "Show Successfull!", data = movieReviewsDictionary)

'''
show movie Information from IMDb

movieId
'''   
@movie_page_Imdb.route("/movieImdbInfo")
def Info():
    import json
    from jsonpath import jsonpath

    req = request.values
    movieId = req['movieId'] if "movieId" in req else ""

    #exampleMovieId = 'tt1375666'

    #call urls
    urls = [
    'https://imdb-api.com/en/API/Reviews/k_ds7a1ynu/' + movieId,
    'https://imdb-api.com/en/API/Title/k_ds7a1ynu/' + movieId,
    'https://imdb-api.com/en/API/Ratings/k_ds7a1ynu/' + movieId,
    'https://imdb-api.com/en/API/FullCast/k_ds7a1ynu/' + movieId,
    'https://imdb-api.com/API/Posters/k_ds7a1ynu/' + movieId,
    'https://api.themoviedb.org/3/movie/' + movieId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1'
    ]

    #call api
    counter = 0
    with FuturesSession() as session:
        futures = [session.get(url) for url in urls]
        for future in futures:
            if counter == 0:
                title = jsonpath(future.result().json(),'$..fullTitle')
                type = jsonpath(future.result().json(),'$..type')
                year = jsonpath(future.result().json(),'$..year')
                print(year)
            elif counter == 1:
                plot = jsonpath(future.result().json(),'$..plot')
            elif counter == 2:
                rating = jsonpath(future.result().json(),'$..imDb')
            elif counter == 3:
                cast = jsonpath(future.result().json(),'$..actors')
            elif counter == 4:
                posters = jsonpath(future.result().json(),'$..posters')
            elif counter == 5:
                tmdbId = jsonpath(future.result().json(),'$.belongs_to_collection..id')
            counter = counter + 1

    plotFinal = ''
    for p in plot:
        if p != '':
            plotFinal = p

    movieInfoDictionary = {
        "title": title,
        "year": year,
        "type": type,
        "plot": plotFinal,
        "cast (actors)": cast,
        "posters": posters,
        "Imdb Rating": rating,
        "Tmdb Id": tmdbId
    }


    return ops_renderJSON(msg = "Show Successfull!", data = movieInfoDictionary)

'''
show movie bottom 10 from IMDb

numberOfMovies
'''   
@movie_page_Imdb.route("/movieImdbBottomInfo")
def bottom():

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
        result = re.search('/title/(.*)/', test)
        theMovieId = result.group(1)

        urls = [
            'https://imdb-api.com/en/API/Ratings/k_ds7a1ynu/' + theMovieId,
            'https://api.themoviedb.org/3/movie/' + theMovieId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1',
            'https://imdb-api.com/API/Posters/k_ds7a1ynu/' + theMovieId
        ]

        counter = 0
        with FuturesSession() as session:
            futures = [session.get(url) for url in urls]
            for future in futures:
                if counter == 0:
                    rating = jsonpath(future.result().json(),'$..imDb')
                elif counter == 1:
                    #posters = jsonpath(future.result().json(),'$..poster_path')
                    tmdbId = jsonpath(future.result().json(),'$..id')
                    genres = jsonpath(future.result().json(),'$.genres..name')
                elif counter == 2:
                    posters = jsonpath(future.result().json(),'$.posters[0]..link')
                counter = counter + 1

        try:
           theTmdbId = tmdbId[0]
        except:
            theTmdbId = 0
            
        data = {"movie_title": movie_title,
                "Imdb_Rating": rating,
                "Imdb_Id": theMovieId,
                "tmdb_Id": theTmdbId,
                "posters": posters,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "genres": genres,
                "link": links[index]}
        list.append(data)
    
    return ops_renderJSON(msg = "Show Comments Successfull!", data = list)

'''
show worst comments


'''   
@movie_page_Imdb.route("/movieImdbLoadWorstComments")
def worst():
    req = request.values
    movieId = req['movieId'] 

    url = 'https://www.imdb.com/title/' + str(movieId) + '/reviews?sort=userRating&dir=asc&ratingFilter=0'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    reviews = soup.select('div.text.show-more__control')
    dates = soup.select('span.review-date')
    displayNames = soup.select('span.display-name-link')

    list = []

    for index in range(0, len(reviews)):
	    review = reviews[index].get_text()
	    date = dates[index].get_text()
	    displayName = displayNames[index].get_text()
	    rating = "1/10"

	    data = {"review": review,
			    "date": date,
			    "username": displayName,
			    "rating": rating}
	    list.append(data)

    return ops_renderJSON(msg = "Show Comments Successfull!", data = list)