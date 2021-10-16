# -*- coding: utf-8 -*-
#Local development environment configuration file
from config.base_setting import *
#SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:123456Egowic@127.0.0.1/movie"
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "123456"
AUTH_COOKIE_NAME = "token"

DOMAIN = {
    "www":"http://127.0.0.3:5000"
}