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
from common.models.userMovies import Usermovy
from tmdbv3api import TMDb
from tmdbv3api import Movie
import json
from jsonpath import jsonpath



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
    userJson = User.serialize(user)
    response = make_response( ops_renderJSON( msg="login successfully!",data = userJson ) )
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                        "%s#%s"%( UserService.geneAuthCode( user ), user.userId ),60 * 60 *24 *7 )
    
    return response

@member_page.route("/logout")
def logOut():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    response = make_response( ops_renderJSON( msg="logout successfully!" ) )
    response.delete_cookie(  app.config['AUTH_COOKIE_NAME'] )
    return response

@member_page.route("/movieLikes")
def movieLikes():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    userId = req['userId'] if 'userId' in req else ''
    movieId = req['movieId'] if 'movieId' in req else ''

    model_movies = Usermovy()
    model_movies.movieId = movieId
    model_movies.userId = userId
    model_movies.type = 1

    db.session.add( model_movies )
    db.session.commit()


    return ops_renderJSON(msg = "Show movieLikes Successfull!")

@member_page.route("/showMovieLikes")
def showMovieLikes():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    #userId = str(current_user.userId)
    movieId = req['movieId'] if "movieId" in req else ""
    textsql = " 1=1 and movieId = "+ movieId + " and useId = "+ userId + " and type = 1"
    result = Usermovy.query.filter(text(textsql)).order_by(Usermovy.Id.desc()).all()
    movieLikes = []
    for userMovies in result:
        userMovie = Serializer.serialize(userMovies)
        movieLikes.append(userMovie)


    return ops_renderJSON( msg = "show movieLikes successfully!",data = movieLikes )


@member_page.route("/showMovieList")
def showMovieList():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    textsql = " 1=1 and userId = "+ userId + " and type = 1"
    result = Usermovy.query.filter(text(textsql)).order_by(Usermovy.Id.desc()).all()
    movieLikes = []
    for userMovies in result:
        userMovie = Serializer.serialize(userMovies)
        movieInfo = {}

        response2 = requests.get('https://api.themoviedb.org/3/movie/' + userMovies.movieId + '?api_key=11fd5ef69d961d91f0f010d0407fd094&language=en-US&page=1')
        genres = jsonpath(response2.json(),'$..genres')

        tmdb = TMDb()
        tmdb.language = 'en'
        tmdb.debug = True
        tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
        movie = Movie()
        m = movie.details(userMovies.movieId)

        movieInfo['genres'] = genres
        movieInfo['title'] = m.title
        movieInfo['poster_path'] = "https://image.tmdb.org/t/p/w500" + m.poster_path
        movieInfo['popularity'] = m.popularity
        movieInfo['vote_average'] = m.vote_average
        movieInfo['release_date'] = m.release_date
        dictMerged2 = dict( userMovie, **movieInfo )
        movieLikes.append(dictMerged2)


    return ops_renderJSON( msg = "show movieLikes successfully!",data = movieLikes )

@member_page.route("/showCommentList")
def showCommentList():
   # response = make_response( redirect( UrlManager.buildUrl("/") ) )
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    textsql = " 1=1 and userId = "+ userId
    
    result = Usercomment.query.filter(text(textsql)).order_by(Usercomment.id.desc()).all()
    movieComments = []
    for comments in result:
        comments.toxic = round(float(comments.toxic), 2)
        comments.sentiment = round(float(comments.sentiment), 2)
        comment = Serializer.serialize(comments)
        movieInfo = {}

        tmdb = TMDb()
        tmdb.language = 'en'
        tmdb.debug = True
        tmdb.api_key = '11fd5ef69d961d91f0f010d0407fd094'
        movie = Movie()
        m = movie.details(comments.movieId)

        movieInfo['title'] = m.title
        movieInfo['poster_path'] = "https://image.tmdb.org/t/p/w500"+ m.poster_path
        movieInfo['popularity'] = m.popularity
        movieInfo['release_date'] = m.release_date
        dictMerged2 = dict( comment, **movieInfo )
        movieComments.append(dictMerged2)


    return ops_renderJSON( msg = "show movieLikes successfully!",data = movieComments )
