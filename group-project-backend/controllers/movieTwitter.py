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


movie_page_Twitter = Blueprint( "movie_page_Twitter",__name__ )

@movie_page_Twitter.route("/movieTwitterReviews")
def review():

    req = request.values
    movieName = req['movieName'] if "movieName" in req else ""

    consumer_key="BtNMua2cnczTyaCIQ0ZKA01xV"
    consumer_secret="dWWqv17X6XKVYm9SrfLr10WrJQHYCYhUjAhxw8DBKdoHBqaTTZ"
    access_token="1444319826399408130-F8gWnTYETTKv5pEXlNSkPoGgDOc0dm"
    access_token_secret="8D4vBQZrcsN3g1wPyfxUItcybcOctf8fioTtbuyfxEfKz"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    cursor = tweepy.Cursor(api.search_tweets, q=str(movieName), tweet_mode="extended").items(30)

    list = []

    for c in cursor:
        list.append(c.full_text)


    return ops_renderJSON(msg = "Show Comments Successfull!", data = list)