# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify
from sqlalchemy import  text
from application import db
from common.models.user import User
from common.models.serializer import Serializer
index_page = Blueprint( "index_page",__name__ )

@index_page.route("/")
def index():
    ##
    name = "imooc"
    ##
    context = { "name" : name }
    context['user'] = { "a":"b","c":"d"}
    context['num_list'] = [ 1,2,3,4,5]

    result = User.query.all()
    context['result'] = result

    return render_template( "index.html",**context )

@index_page.route("/json")
def json():
    import json
    data = {}
    result = User.query.all()
    data['result'] = result
    #response = make_response( json.dumps( data ) )
    response = make_response( json.dumps( User.serialize_list(result) ) )
    response.headers["Content-Type"] = "application/json"
    return response

@index_page.route("/userInfo")
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

@index_page.route( "/json2" )
def json_same():
    data = { "a":"b" }
    result = User.query.all()
    payload = []
    data['result'] = ''.join(result)
    response = make_response( jsonify( data )  )
    return response

@index_page.route("/json3")
def ret():
    data = {"a":"b"}
    sql = text( "select * from `user`")
    result = db.engine.execute( sql )
    #data['result'] = result
    ...
    for row in result:
        # Python dict
        data = {}
        # 将row中的每个元素，追加到字典中。
    

    response = make_response( jsonify( data )  )
    return response