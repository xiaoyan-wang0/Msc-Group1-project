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
#from controllers.index import index_page
from controllers.member import member_page
from controllers.movieImdb import movie_page_Imdb
from controllers.movieTmdb import movie_page_Tmdb
from controllers.movieYoutube import movie_page_Youtube
from controllers.movieTwitter import movie_page_Twitter
#from controllers.movieRecommandation import movie_page_Recommandation
from controllers.comments import comments_page
from controllers.recomendation import rec_page
from controllers.admin import admin_page

#app.register_blueprint( index_page,url_prefix = "/" )
app.register_blueprint( member_page,url_prefix = "/member" )
app.register_blueprint( movie_page_Imdb,url_prefix = "/movieImdb" )
app.register_blueprint( movie_page_Tmdb,url_prefix = "/movieTmdb" )
app.register_blueprint( movie_page_Youtube,url_prefix = "/movieYoutube" )
app.register_blueprint( movie_page_Twitter,url_prefix = "/movieTwitter" )
#app.register_blueprint( movie_page_Recommandation,url_prefix = "/movieRecommandation" )
app.register_blueprint( comments_page,url_prefix = "/comments" )
app.register_blueprint( rec_page,url_prefix = "/rec" )
app.register_blueprint( admin_page,url_prefix = "/admin" )

'''
template url
'''
from common.libs.UrlManager import UrlManager
app.add_template_global( UrlManager.buildUrl,'buildUrl' )