# -*- coding: utf-8 -*-
#Local development environment configuration file
from config.base_setting import *
#SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:qq123@127.0.0.1/movie?autocommit=true"
SQLALCHEMY_ECHO = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = Flase
SQLALCHEMY_POOL_SIZE = 25
SQLALCHEMY_MAX_OVERFLOW = 10

SECRET_KEY = "123456"
AUTH_COOKIE_NAME = "token"

DOMAIN = {
    "www":"http://127.0.0.3:5000"
}