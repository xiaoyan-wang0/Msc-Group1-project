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
import tweepy
import pandas as pd
from common.libs.Sentiment import sentiment
from common.models.reviews import Review
import json


movie_page_Twitter = Blueprint( "movie_page_Twitter",__name__ )

@movie_page_Twitter.route("/movieTwitterReviews")
def review():

    req = request.values
    movieName = req['movieName'] if "movieName" in req else ""

    movieId = req['movieId'] if "movieId" in req else ""
    type = str(4)
    textsql = " 1=1 and movieId = "+movieId+" and type = "+ type
    result = Review.query.filter(text(textsql)).order_by(Review.reviewId.desc()).limit(1).first()
    if  result:
        return ops_renderJSON(msg = "Show Successfull!", data = result.content)

    consumer_key="BtNMua2cnczTyaCIQ0ZKA01xV"
    consumer_secret="dWWqv17X6XKVYm9SrfLr10WrJQHYCYhUjAhxw8DBKdoHBqaTTZ"
    access_token="1444319826399408130-F8gWnTYETTKv5pEXlNSkPoGgDOc0dm"
    access_token_secret="8D4vBQZrcsN3g1wPyfxUItcybcOctf8fioTtbuyfxEfKz"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # To be added: Search tweets according to page number...
    cursor = tweepy.Cursor(api.search_tweets, q=str(movieName), tweet_mode="extended", lang='en').items(20)

    list = []


    # for c in cursor:
    #     list.append(c.full_text)

    dic2= []
    for c in cursor:
        dic = {}
        content =  [c.full_text]
        dic['content'] = c.full_text
        result = detector(content)
        dic['toxic'] = result['tag']
        senti = sentiment(content)
        dic['sentiment'] = senti['tag']
        dic2.append(dic)


    model_reviews = Review()
    model_reviews.content = dic2
    model_reviews.movieId = movieId
    model_reviews.type = 4

    db.session.add( model_reviews )
    db.session.commit()
    db.session.close()
    db.engine.dispose()

    return ops_renderJSON(msg = "Show Comments Successfull!", data = dic2)