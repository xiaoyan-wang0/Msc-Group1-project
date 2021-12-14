# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify,redirect,Response
import requests
from sqlalchemy import  text
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.usercomments import Usercomment
from common.models.userInfo import Userinfo
from common.models.userInfo2 import Userinfo2
#import cv2
import numpy as np
from common.models.serializer import Serializer
from common.libs.UserService import UserService
from common.libs.ToxicComments import do_pe,detector
from common.models.userMovies import Usermovy
from tmdbv3api import TMDb
from tmdbv3api import Movie
import json
from jsonpath import jsonpath
import base64
import time

admin_page = Blueprint( "admin_page",__name__ )

@admin_page.route("/doReport")
def doReport():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    id = req['id'] if "id" in req else ""
    result = Usercomment.query.filter_by( id = id ).first()

    if result and result.ifReport == 0:
        db.session.query(Usercomment).filter(Usercomment.id == id).update({"ifReport":1,"reporterId":userId})

    db.session.close()
    db.engine.dispose()

    return ops_renderJSON( msg = "report successfully!")


@admin_page.route("/getReportComments")
def getReportComments():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    #req = request.values
    #userId = req['userId'] if "userId" in req else ""
    result = Usercomment.query.filter(Usercomment.ifReport == '1').order_by(Usercomment.id.desc()).all()
    db.session.close()
    db.engine.dispose()
    result = Serializer.serialize_list(result)
    return ops_renderJSON( msg = "report successfully!", data = result)

@admin_page.route("/adminLogin", methods = ["POST" ])
def adminLogin():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    name = req['name'] if "name" in req else ""
    password = req['password'] if "password" in req else ""
    
    if name != 'admin' or password !='1234567':
        return ops_renderErrJSON( msg = "error" )

    return ops_renderJSON( msg = "login successfully!")

@admin_page.route("/userList")
def userList():
    
    users = User.query.all()
    List = []
    for user in users:
        userInfo = Userinfo2.query.filter_by( userId = user.userId ).first()
        db.session.close()
        db.engine.dispose()
        user = Serializer.serialize(user)
        userInfo = Serializer.serialize(userInfo)
        List.append(dict( user, **userInfo ))

    return ops_renderJSON( msg = "login successfully!",data = List)

@admin_page.route("/commentsList")
def commentsList():
    
    commentsList = Usercomment.query.all()
    commentsList = Serializer.serialize_list(commentsList)

    return ops_renderJSON( msg = "login successfully!",data = commentsList)

@admin_page.route("/getSentimentRate")
def getSentimentRate():
    
    req = request.values
    
    #sql = 'SELECT DISTINCT movieId,createTime FROM recommandation WHERE userId = ' +userId+ ' ORDER BY createTime DESC LIMIT 5;'
    sql = 'SELECT SUM(case WHEN sentiment = 1 then 1 else 0 end ) as positive,  SUM(case WHEN sentiment = 0 then 1 else 0 end ) as negative, SUM(case WHEN sentiment = 2 then 1 else 0 end ) as neutral FROM usercomments ;'
    result = db.session.execute(text(sql)).fetchall()
    List = {}
    for lis in result:
        List['positive'] = str(lis[0])
        List['negative'] = str(lis[1])
        List['neutral'] = str(lis[2])
    return ops_renderJSON( msg = "get SentimentRate successfully!",data = List)

@admin_page.route("/getToxicRate")
def getToxicRate():
    
    req = request.values

    #sql = 'SELECT DISTINCT movieId,createTime FROM recommandation WHERE userId = ' +userId+ ' ORDER BY createTime DESC LIMIT 5;'
    sql = 'SELECT SUM(case WHEN toxic <= 0.53 then 1 else 0 end ) as toxic,  SUM(case WHEN toxic > 0.53 AND toxic < 0.9 then 1 else 0 end ) as midToxic, SUM(case WHEN toxic >= 0.9 then 1 else 0 end ) as noneToxic FROM usercomments ;'
    result = db.session.execute(text(sql)).fetchall()
    List = {}
    for lis in result:
        List['toxic'] = str(lis[0])
        List['midToxic'] = str(lis[1])
        List['noneToxic'] = str(lis[2])
    return ops_renderJSON( msg = "get toxicRate successfully!",data = List)


@admin_page.route("/blockUser")
def blockUser():
    
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    
    if userId != "":
        user = User.query.filter_by( userId = userId ).first()
        if user:
            db.session.query(User).filter(User.userId == userId).update({"ifBlocked":1})
            db.session.close()
            db.engine.dispose()
    return ops_renderJSON( msg = "block user successfully!")

@admin_page.route("/deleteComments")
def deleteComments():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    id = req['id'] if "id" in req else ""
    try:
        db.session.query(Usercomment).filter(Usercomment.id == id).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()  
        raise e
    finally:
        db.session.close()
        db.engine.dispose()
    time.sleep(1.5)
    return ops_renderJSON( msg = "delete comment successfully!")

@admin_page.route("/unBlockUser")
def unBlockUser():
    
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    
    if userId != "":
        user = User.query.filter_by( userId = userId ).first()
        if user:
            db.session.query(User).filter(User.userId == userId).update({"ifBlocked":0})
            db.session.close()
            db.engine.dispose()
    
    return ops_renderJSON( msg = "block user successfully!")

@admin_page.route("/getUser")
def getUser():
    
    req = request.values
    email = req['email'] if "email" in req else ""    
    user = User.query.filter_by( email = email ).first()
    if not user:
        return ops_renderErrJSON( msg = "error" )
    user = Serializer.serialize(user)

    return ops_renderJSON( msg = "find user successfully!",data = user)