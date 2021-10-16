# -*- coding: utf-8 -*-
from application import app


from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension( app )

'''
Interceptor processing and error handler
'''
from interceptors.Auth import *
from interceptors.errorHandler import *

'''
path url
'''
from controllers.index import index_page
from controllers.member import member_page
from controllers.movieImdb import movie_page
from controllers.movieTmdb import movie_page

app.register_blueprint( index_page,url_prefix = "/" )
app.register_blueprint( member_page,url_prefix = "/member" )
app.register_blueprint( movie_page,url_prefix = "/movie" )
app.register_blueprint( movie_page,url_prefix = "/movie" )

'''
template url
'''
from common.libs.UrlManager import UrlManager
app.add_template_global( UrlManager.buildUrl,'buildUrl' )