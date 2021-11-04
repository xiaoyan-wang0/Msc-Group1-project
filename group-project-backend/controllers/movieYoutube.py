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

    response = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=' + str(movieName) + ' trailer' + '&type=video&key=AIzaSyCL_TmpbiATD9nisVU-TAbXCOZ6n1mu__E')
    trailerId = jsonpath(response.json(),'$..videoId')

    trailerIdToString = str(trailerId)[2:13]

    response2 = requests.get('https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=' + trailerIdToString + '&key=AIzaSyCL_TmpbiATD9nisVU-TAbXCOZ6n1mu__E')
    reviews = jsonpath(response2.json(),'$..textDisplay')
    names = jsonpath(response2.json(),'$..authorDisplayName')
    profileImages = jsonpath(response2.json(),'$..authorProfileImageUrl')
    times = jsonpath(response2.json(),'$..publishedAt')
    

    list = []

    #item_dict = json.loads(names)

    #print(len(item_dict['authorDisplayName']))
    aList = json.loads(names)
    for i in range(0, iter(aList)):
    #for i in range(0, len(names)):
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

    return ops_renderJSON(msg = "Show Successfull!", data = list)