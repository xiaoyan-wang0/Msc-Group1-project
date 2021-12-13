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
from jsonpath import jsonpath
from common.libs.Sentiment import sentiment
from common.models.reviews import Review


movie_page_Youtube = Blueprint( "movie_page_Youtube",__name__ )

@movie_page_Youtube.route("/movieYoutubeReviews")
def review():

    import json

    # if 'current_user' in  g:
    #     current_user = g.current_user
    # if current_user == None : 
    #     return ops_renderErrJSON( msg ="please login first")

    # Time, user name, user image, comments

    req = request.values
    movieName = req['movieName'] 

    movieId = req['movieId'] if "movieId" in req else ""
    type = str(3)
    textsql = " 1=1 and movieId = "+movieId+" and type = "+ type
    result = Review.query.filter(text(textsql)).order_by(Review.reviewId.desc()).limit(1).first()
    if  result:
        return ops_renderJSON(msg = "Show Successfull!", data = result.content)

    try:
        #There are daily limits for the keys
        key1 = 'AIzaSyCL_TmpbiATD9nisVU-TAbXCOZ6n1mu__E'
        key2 = 'AIzaSyC6cz_fRdiwLhdlPBpkhyr0MXzF0PXMA4o'

        response = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=' + str(movieName) + ' trailer' + '&type=video&key=' + key2)
        trailerId = jsonpath(response.json(),'$..videoId')

        print(trailerId)

        trailerIdToString = str(trailerId)[2:13]

        response2 = requests.get('https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=' + trailerIdToString + '&key=' + key2)
        reviews = jsonpath(response2.json(),'$..textDisplay')
        names = jsonpath(response2.json(),'$..authorDisplayName')
        profileImages = jsonpath(response2.json(),'$..authorProfileImageUrl')
        times = jsonpath(response2.json(),'$..publishedAt')
        

        list = []

        #item_dict = json.loads(names)

        #print(len(item_dict['authorDisplayName']))
        #aList = json.loads(names)

        #return response2.json()
        #for i in range(0, iter(names)):
        for i in range(0, len(names)):
            content = [reviews[i]]
            result = detector(content)
            senti = sentiment(content)
            youtubeInfoDictionary = {
            "username": names[i],
            "review": reviews[i],
            "toxic": result['tag'],
            "sentiment": senti['tag'],
            "profile_picture": profileImages[i],
            "time": times[i]
            }
            list.append(youtubeInfoDictionary)

        model_reviews = Review()
        model_reviews.content = list
        model_reviews.movieId = movieId
        model_reviews.type = 3
        db.session.add( model_reviews )
        db.session.commit()
        db.session.close()
        db.engine.dispose()
        
    except Exception:
        return ops_renderJSON(msg = "Show Successfull!")


    return ops_renderJSON(msg = "Show Successfull!", data = list)