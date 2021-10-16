# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify,redirect
import requests
from sqlalchemy import  text
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.usercomments import Usercomment
from common.models.serializer import Serializer
from common.libs.UserService import UserService
from common.libs.ToxicComments import do_pe,detector


from json import load as json_load
import json
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import pickle

import numpy as np


member_page = Blueprint( "member_page",__name__ )

@member_page.route("/reg",methods = [ "POST" ])
def reg():

    req = request.values
    userName = req['userName'] if "userName" in req else ""
    email = req['email'] if "email" in req else ""
    password = req['password'] if "password" in req else ""

    if userName is None or len( userName ) < 1:
        return ops_renderErrJSON( msg = "userName error" )

    if password is None or len( password ) < 6:
        return ops_renderErrJSON( msg ="password must more then 6 character")

    user_info = User.query.filter_by( email = email ).first()
    if user_info:
        return ops_renderErrJSON( msg ="email already registered")

    model_user = User()
    model_user.userName = userName
    model_user.email = email
    model_user.password = UserService.genePwd( password )
    db.session.add( model_user )
    db.session.commit()

    return ops_renderJSON( msg = "register successfully!")

@member_page.route("/login",methods = ["POST" ])
def login():

    req = request.values
    email = req['email'] if 'email' in req else ''
    password = req['password'] if 'password' in req else ''
    if email is None or len( email ) < 1:
        return ops_renderErrJSON(  "Please enter the correct email" )

    if password is None or len( password ) < 6:
        return ops_renderErrJSON("Please enter the correct password")
    user = User.query.filter_by( email = email ).first()
    if not user:
        return ops_renderErrJSON("email not exist")

    if user.password != UserService.genePwd( password ):
        return ops_renderErrJSON("password error")

    response = make_response( ops_renderJSON( msg="login successfully!" ) )
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                        "%s#%s"%( UserService.geneAuthCode( user ), user.userId ),60 * 60 *24 *7 )
    return response

@member_page.route("/logout")
def logOut():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    response = make_response( ops_renderJSON( msg="logout successfully!" ) )
    response.delete_cookie(  app.config['AUTH_COOKIE_NAME'] )
    return response


@member_page.route("/addComments")
def addComments():
    import json
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    comment = req['comment'] if "comment" in req else ""
    movieId = req['movieId'] if "movieId" in req else ""
    
    model_comments = Usercomment()
    model_comments.userId = userId
    model_comments.comment = comment
    model_comments.movieId = movieId
    db.session.add( model_comments )
    db.session.commit()
    
    return ops_renderJSON( msg = "addComments successfully!")

@member_page.route("/showComments")
def showComments():
    import json
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    movieId = req['movieId'] if "movieId" in req else ""
    textsql = " 1=1 and userId = '"+userId+"' and movieId = '"+movieId+"'"
    result = Usercomment.query.filter(text(textsql)).all()
    usercomments = Usercomment.serialize_list(result)
    #response = make_response( json.dumps( data ) )
    return ops_renderJSON( msg = "showComments successfully!",data = usercomments )

@member_page.route("/toxic")
def toxic():

    req = request.values
    title = [req['title'] if "title" in req else ""]
    
    result = detector(title)
    
    return ops_renderJSON( msg = "comments detected successfully!",data = result )


