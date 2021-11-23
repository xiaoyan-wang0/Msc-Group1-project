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

comments_page = Blueprint( "comments_page",__name__ )

@comments_page.route("/addComments",methods = ["POST" ])
def addComments():
    import json

    '''
    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
    ''' 

    req = request.values
    userId = req['userId'] if "userId" in req else ""

    user = User.query.filter_by( userId = userId ).first()
    if user:
        if user.ifBlocked == 1:
            return ops_renderErrJSON( msg = "use have been blocked" )

    #userId = str(current_user.userId)
    comment = req['comment'] if "comment" in req else ""
    movieId = req['movieId'] if "movieId" in req else ""
    comment = [comment]
    result = detector(comment)
    senti = sentiment(comment)
    toxic = result['tag']
    sentiment2 = senti['tag']
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
    return ops_renderJSON( msg = "addComments successfully!")

@comments_page.route("/showComments")
def showComments():
    import json
    '''
    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
    '''
    req = request.values
    userId = req['userId'] if "userId" in req else ""
    #userId = str(current_user.userId)
    movieId = req['movieId'] if "movieId" in req else ""
    textsql = " 1=1 and movieId = '" + movieId + "'"
    result = Usercomment.query.filter(text(textsql)).order_by(Usercomment.id.desc()).all()

    comments = []
    #usercomments = Usercomment.serialize_list(result)
    for comment in result:
        user = User.query.filter_by( userId = comment.userId ).first()
        if user:       
            user = User.serialize(user)
            comment = Serializer.serialize(comment)
            dictMerged2 = dict( comment, **user )
            comments.append(dictMerged2)
            
        db.session.close()
    return ops_renderJSON( msg = "showComments successfully!",data = comments )

@comments_page.route("/toxic",methods = ["POST" ])
def toxic():
    '''
    if 'current_user' in  g:
        current_user = g.current_user
    if current_user == None : 
        return ops_renderErrJSON( msg ="please login first")
    '''    
    req = request.values
    title = [req['title'] if "title" in req else ""]
    toxic = detector(title)
    senti = sentiment(title)
    result = {"toxic" : toxic['tag']}
    result['sentiment'] = senti['tag']
    return ops_renderJSON( msg = "comments detected successfully!",data = result )