from flask import Blueprint,render_template,request,make_response,jsonify,redirect
from sqlalchemy import  text
from application import app,db
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.models.usercomments import Usercomment
from common.models.serializer import Serializer
from common.libs.UserService import UserService


movie_page = Blueprint( "movie_page",__name__ )

@movie_page.route("/userInfo")
def test():
    import json
    data = {}
    result = User.query.all()
    #data['result'] = result
    data['code'] = '100'
    data['result'] = User.serialize_list(result)
    #response = make_response( json.dumps( data ) )
    response = make_response( json.dumps( data ) )
    response.headers["Content-Type"] = "application/json"
    return response