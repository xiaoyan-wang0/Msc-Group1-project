# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from common.models.serializer import Serializer

db = SQLAlchemy()



class Userinfo(db.Model):
    __tablename__ = 'userinfo'

    userInfoId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    image = db.Column(db.LONGBLOB)
    birthday = db.Column(db.DateTime)
    likeNum = db.Column(db.Integer)
    followNum = db.Column(db.Integer)
    age = db.Column(db.Integer)
    overView = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'))
    movieTags = db.Column(db.String(64))

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d