# -*- coding: utf-8 -*-
#Local development environment configuration file
from config.base_setting import *
#SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:qq123@127.0.0.1/movie?autocommit=true"
SQLALCHEMY_ECHO = False
#SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_POOL_TIMEOUT=10
SQLALCHEMY_POOL_SIZE = 0
SQLALCHEMY_MAX_OVERFLOW = -1

from sqlalchemy.pool import StaticPool
#SQLALCHEMY_ENGINE_OPTIONS = {"poolclass":"NullPool"}
# SQLALCHEMY_ENGINE_OPTIONS = {
#     "poolclass": StaticPool
# }
SECRET_KEY = "123456"
AUTH_COOKIE_NAME = "token"

DOMAIN = {
    "www":"http://127.0.0.3:5000"
}