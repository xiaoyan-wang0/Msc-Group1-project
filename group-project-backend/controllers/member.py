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
import time
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



member_page = Blueprint( "member_page",__name__ )

'''
registration
POST

userName
email
password

'''
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

    #save to database
    model_user = User()
    model_user.userName = userName
    model_user.email = email
    model_user.password = UserService.genePwd( password )

    try:
        db.session.add( model_user )
        db.session.commit()
    except Exception as e:
        db.session.rollback()  
        raise e
    finally:
        db.session.close()
        db.engine.dispose()

    #save user Information
    newUser = User.query.filter_by( email = email ).first()

    model_userInfo = Userinfo()
    model_userInfo.userId = newUser.userId
    db.session.add( model_userInfo )
    db.session.commit()

    userInfo = Userinfo.query.filter_by( userId = newUser.userId ).first()
    userInfo = Userinfo.serialize(userInfo)
    newUser = User.serialize(newUser)
    dictMerged2 = dict( newUser, **userInfo )
    db.session.close()
    db.engine.dispose()

    return ops_renderJSON( msg = "register successfully!",data = dictMerged2)


'''
login
POST

email
password
'''
@member_page.route("/login",methods = ["POST" ])
def login():

    req = request.values
    email = req['email'] if 'email' in req else ''
    password = req['password'] if 'password' in req else ''

    if email is None or len( email ) < 1:
        return ops_renderErrJSON(  "Please enter the correct email" )

    if password is None or len( password ) < 6:
        return ops_renderErrJSON("Please enter the correct password")
    
    #check if user exist
    user = User.query.filter_by( email = email ).first()
    if not user:
        return ops_renderErrJSON("email not exist")

    if user.password != UserService.genePwd( password ):
        return ops_renderErrJSON("password error")

    #get user Information
    userInfo = Userinfo.query.filter_by( userId = user.userId ).first()
    userInfo.image = ""
    userInfo = Userinfo.serialize(userInfo)

    #make response
    dictMerged2 = dict( User.serialize(user), **userInfo )
    response = make_response( ops_renderJSON( msg="login successfully!",data = dictMerged2 ) )
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                        "%s#%s"%( UserService.geneAuthCode( user ), user.userId ),60 * 60 *24 *7 )
    
    return response

'''
logout

'''
@member_page.route("/logout")
def logOut():

    #move cookie
    response = make_response( ops_renderJSON( msg="logout successfully!" ) )
    response.delete_cookie(  app.config['AUTH_COOKIE_NAME'] )
    return response


'''
add a movie to user like list

userId
movieId
'''
@member_page.route("/movieLikes")
def movieLikes():

    req = request.values
    userId = req['userId'] if 'userId' in req else ''
    movieId = req['movieId'] if 'movieId' in req else ''

    #select
    textsql = " 1=1 and movieId = "+ movieId + " and userId = "+ userId + " and type = 1"
    usermovy = Usermovy.query.filter(text(textsql)).all()

    #check if already likes
    if usermovy:
        return ops_renderErrJSON( msg ="user already liked")

    #add to database
    model_movies = Usermovy()
    model_movies.movieId = movieId
    model_movies.userId = userId
    model_movies.type = 1

    try:
        db.session.add( model_movies )
        db.session.commit()
    except Exception as e:
        db.session.rollback()  
        raise e
    finally:
        db.session.close()
        db.engine.dispose()

    return ops_renderJSON(msg = "Show movieLikes Successfull!")

'''
show movies that the user likes

userId
movieId
'''
@member_page.route("/showMovieLikes")
def showMovieLikes():

    req = request.values
    userId = req['userId'] if "userId" in req else ""
    movieId = req['movieId'] if "movieId" in req else ""

    #select database
    textsql = " 1=1 and movieId = "+ movieId + " and userId = "+ userId + " and type = 1"
    result = Usermovy.query.filter(text(textsql)).order_by(Usermovy.Id.desc()).all()

    movieLikes = []
    for userMovies in result:
        userMovie = Serializer.serialize(userMovies)
        movieLikes.append(userMovie)


    return ops_renderJSON( msg = "show movieLikes successfully!",data = movieLikes )

'''
show movies that the user likes

userId
movieId
'''
@member_page.route("/showMovieList")
def showMovieList():

    req = request.values
    userId = req['userId'] if "userId" in req else ""

    #select
    textsql = " 1=1 and userId = "+ userId + " and type = 1"
    result = Usermovy.query.filter(text(textsql)).order_by(Usermovy.Id.desc()).all()
    movieLikes = []
    for userMovies in result:
        userMovie = Serializer.serialize(userMovies)
        movieInfo = {}

        #call TMDb api to get movie information based on movieId
        response2 = requests.get('https://api.themoviedb.org/3/movie/' + userMovies.movieId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
        genres = jsonpath(response2.json(),'$..genres')

        tmdb = TMDb()
        tmdb.language = 'en'
        tmdb.debug = True
        tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
        movie = Movie()
        m = movie.details(userMovies.movieId)

        #Setting JSON parameters
        movieInfo['genres'] = genres
        movieInfo['title'] = m.title
        movieInfo['poster_path'] = "https://image.tmdb.org/t/p/w500" + m.poster_path
        movieInfo['popularity'] = m.popularity
        movieInfo['vote_average'] = m.vote_average
        movieInfo['release_date'] = m.release_date
        dictMerged2 = dict( userMovie, **movieInfo )
        movieLikes.append(dictMerged2)


    return ops_renderJSON( msg = "show movieLikes successfully!",data = movieLikes )

'''
show the user comments

userId
movieId
'''
@member_page.route("/showCommentList")
def showCommentList():

    req = request.values
    userId = req['userId'] if "userId" in req else ""
    textsql = " 1=1 and userId = "+ userId
    
    #reduce server concurrent
    time.sleep(1)

    #get from database
    result = Usercomment.query.filter(text(textsql)).order_by(Usercomment.id.desc()).all()
    movieComments = []

    for comments in result:

        comments.toxic = round(float(comments.toxic), 2)
        comments.sentiment = round(float(comments.sentiment), 2)
        comment = Serializer.serialize(comments)
        movieInfo = {}

        #call TMDb api to get movie information based on movieId
        tmdb = TMDb()
        tmdb.language = 'en'
        tmdb.debug = True
        tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
        movie = Movie()
        m = movie.details(comments.movieId)

        #setting JSON parameters
        movieInfo['title'] = m.title
        movieInfo['poster_path'] = "https://image.tmdb.org/t/p/w500"+ m.poster_path
        movieInfo['popularity'] = m.popularity
        movieInfo['release_date'] = m.release_date
        dictMerged2 = dict( comment, **movieInfo )
        movieComments.append(dictMerged2)


    return ops_renderJSON( msg = "show commentList successfully!",data = movieComments )

'''
delete the user comments

id -> commentsId
userId
movieId
'''
@member_page.route("/deleteComment")
def deleteComment():
    req = request.values
    id = req['id'] if "id" in req else ""

    #delete from database
    try:
        db.session.query(Usercomment).filter(Usercomment.id == id).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()  
        raise e
    finally:
        db.session.close()
        db.engine.dispose()

    #reduce server concurrent
    time.sleep(1.5)

    return ops_renderJSON( msg = "delete comment successfully!")

'''
delete the user comments

Id -> userMoviesId
'''
@member_page.route("/deleteMovieLikes")
def deleteMovieLikes():

    req = request.values
    Id = req['Id'] if "Id" in req else ""

    #delete from database
    try:
        db.session.query(Usermovy).filter(Usermovy.Id == Id).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()  
        raise e
    finally:
        db.session.close()
        db.engine.dispose()

    #reduce server concurrent
    time.sleep(1.5)

    return ops_renderJSON( msg = "delete movieLikes successfully!")


'''
Upload images
POST

userId
avatar -> image file
'''
@member_page.route("/newUserImage",methods = ["POST" ])
def newUserImage():

    req = request.values
    userId = req['userId'] if "userId" in req else ""
    image = req['avatar'] if "avatar" in req else ""

    #read file
    image = request.files['avatar'].read()

    img = base64.b64decode(image)

    #update user image
    db.session.query(Userinfo).filter(Userinfo.userId == userId).update({"image":image})
    db.session.commit()
    db.session.close()
    db.engine.dispose()

    db.session.query(Userinfo).filter(Userinfo.userId == userId).update({"mimetype":request.files['avatar'].mimetype})
    db.session.commit()
    db.session.close()
    db.engine.dispose()

    return ops_renderJSON( msg = "image updated")

'''
get user image

userId
'''
@member_page.route("/getUserImage")
def getUserImage():

    req = request.values
    userId = req['userId'] if "userId" in req else ""

    userInfo = Userinfo.query.filter_by( userId = userId ).first()
    #check if exist
    if not userInfo:
        return ops_renderErrJSON( msg ="userId not true")
    
    return Response(userInfo.image, mimetype=userInfo.mimetype)

'''
get user infomation

userId
'''
@member_page.route("/getUserInfo")
def getUserInfo():
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    
    
    user = User.query.filter_by( userId = userId ).first()
    userInfo = Userinfo.query.filter_by( userId = userId ).first()
    user = User.serialize(user)
    userInfo.image = ""
    userInfo = Userinfo.serialize(userInfo)
    dictMerged2 = dict( user, **userInfo )

    return ops_renderJSON( msg = "getUserInfo",data = dictMerged2)


'''
set user infomation
POST

userId
userName
email
password
birthday
movieTags
overview
'''
@member_page.route("/setUserInfo",methods = ["POST" ])
def setUserInfo():

    req = request.values
    userId = req['userId'] if "userId" in req else ""
    userName = req['userName'] if "userName" in req else ""
    email = req['email'] if "email" in req else ""
    password = req['password'] if "password" in req else ""
    birthday = req['birthday'] if "birthday" in req else ""
    movieTags = req['movieTags'] if "movieTags" in req else ""
    overview = req['overview'] if "overview" in req else ""
    
    user = User.query.filter_by( userId = userId ).first()

    #check if user exist
    if userId == "":
        return ops_renderErrJSON( msg ="userId not true")
    
    if not user:
        return ops_renderErrJSON( msg ="userId not true")

    #update user Infomation
    if userName != "":
        db.session.query(User).filter(User.userId == userId).update({"userName":str(userName)})

    if email != "":
        db.session.query(User).filter(User.userId == userId).update({"email":str(email)})

    if password != "":
        password = UserService.genePwd( password )
        db.session.query(User).filter(User.userId == userId).update({"password":str(password)})
    
    if birthday != "":
        db.session.query(Userinfo).filter(Userinfo.userId == userId).update({"birthday":str(birthday)})

    if movieTags != "":
        db.session.query(Userinfo).filter(Userinfo.userId == userId).update({"movieTags":str(movieTags)})

    if overview != "":
        db.session.query(Userinfo).filter(Userinfo.userId == userId).update({"overView":str(overview)})

    db.session.close()
    db.engine.dispose()
    
    return ops_renderJSON( msg = "update sucessful")

