from flask import Blueprint,request,make_response,jsonify,redirect,g        
from sqlalchemy import  text
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render


from common.models.user import User
from common.models.usercomments import Usercomment
from common.models.serializer import Serializer
from common.libs.UserService import UserService
from common.libs.ToxicComments import do_pe,detector
from common.libs.Sentiment import sentiment

import requests

import time
comments_page = Blueprint( "comments_page",__name__ )

'''
add one comment 
POST method

userId
comment
movieId
'''
@comments_page.route("/addComments",methods = ["POST" ])
def addComments():
    import json

    req = request.values
    userId = req['userId'] if "userId" in req else ""

    user = User.query.filter_by( userId = userId ).first()
    #check if user exist
    if user:
        #check if user already blocked
        if user.ifBlocked == 1:
            return ops_renderErrJSON( msg = "user have been blocked" )


    comment = req['comment'] if "comment" in req else ""
    movieId = req['movieId'] if "movieId" in req else ""

    comment = [comment]

    #call detector
    result = detector(comment)
    senti = sentiment(comment)
    toxic = result['tag']
    sentiment2 = senti['tag']

    #add to database
    model_comments = Usercomment()
    model_comments.toxic = toxic
    model_comments.sentiment = sentiment2
    model_comments.comment = comment
    model_comments.movieId = movieId
    model_comments.userId = userId
    model_comments.ifReport = 0
    try:
        db.session.add( model_comments )
        db.session.commit()
    except Exception as e:
        db.session.rollback()  
        raise e
    finally:
        db.session.close()
        db.engine.dispose()

    #reduce server concurrent
    time.sleep(1.5)

    return ops_renderJSON( msg = "addComments successfully!")

'''
show all AMDb comments in the movie

userId
movieId
'''
@comments_page.route("/showComments")
def showComments():
    import json

    req = request.values
    userId = req['userId'] if "userId" in req else ""
    movieId = req['movieId'] if "movieId" in req else ""

    #get comments from database
    textsql = " 1=1 and movieId = '" + movieId + "'"
    result = Usercomment.query.filter(text(textsql)).order_by(Usercomment.id.desc()).all()

    comments = []
    for comment in result:
        user = User.query.filter_by( userId = comment.userId ).first()

        #check if user exist
        if user:       
            user = User.serialize(user)
            comment = Serializer.serialize(comment)
            dictMerged2 = dict( comment, **user )
            comments.append(dictMerged2)
            
        db.session.close()
        db.engine.dispose()

    return ops_renderJSON( msg = "showComments successfully!",data = comments )

'''
detect toxic rate

title
'''
@comments_page.route("/toxic",methods = ["POST" ])
def toxic():


    req = request.values
    title = [req['title'] if "title" in req else ""]

    #call detector
    toxic = detector(title)
    senti = sentiment(title)

    #setting parameters
    result = {"toxic" : toxic['tag']}
    result['sentiment'] = senti['tag']

    return ops_renderJSON( msg = "comments detected successfully!",data = result )

'''
Each time the request ends, the connection is automatically closed

'''
@app.teardown_appcontext
def teardown_db(exception):
    
    db.engine.dispose()