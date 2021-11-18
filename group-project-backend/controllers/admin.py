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


admin_page = Blueprint( "admin_page",__name__ )

@admin_page.route("/doReport")
def doReport():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    #userId = req['userId'] if "userId" in req else ""
    id = req['id'] if "id" in req else ""
    result = Usercomment.query.filter_by( id = id ).first()

    if result and result.ifReport == 0:
        db.session.query(Usercomment).filter(Usercomment.id == id).update({"ifReport":1})

    db.session.close()

    return ops_renderJSON( msg = "report successfully!")


@admin_page.route("/getReportComments")
def getReportComments():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    #req = request.values
    #userId = req['userId'] if "userId" in req else ""
    result = Usercomment.query.filter(Usercomment.ifReport == '1').order_by(Usercomment.id.desc()).all()
    db.session.close()
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
