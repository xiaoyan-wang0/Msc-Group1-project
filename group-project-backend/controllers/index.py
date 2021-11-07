# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,jsonify
from sqlalchemy import  text
from application import db
from common.models.user import User
from common.models.serializer import Serializer
from common.libs.ToxicComments import do_pe,detector
from common.libs.Sentiment import sentiment
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render

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
    #str = '[We and our partners store and/or access information on a device, such as cookies and process personal data, such as unique identifiers and standard information sent by a device for personalised ads and content, ad and content measurement, and audience insights, as well as to develop and improve products.With your permission we and our partners may use precise geolocation data and identification through device scanning. You may click to consent to our and our partners’ processing as described above. Alternatively you may click to refuse to consent or access more detailed information and change your preferences before consenting.Please note that some processing of your personal data may not require your consent, but you have a right to object to such processing. Your preferences will apply to this website only. You can change your preferences at any time by returning to this site or visit our privacy policy.]'
    str2 = '[hello]'
    for i in range(1):
        result = detector(str2)
        senti = sentiment(str2)

    return ops_renderJSON(msg = "Show Successfull!")

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

@index_page.route("/sen")
def sen():
    import json
    data = {}
    data2 = {}
    req = request.values
    title = req['title'] if "title" in req else ""
    result = sentiment(title)
    #response = make_response( json.dumps( data ) )
    response = make_response( result )
    response.headers["Content-Type"] = "application/json"
    return response 
