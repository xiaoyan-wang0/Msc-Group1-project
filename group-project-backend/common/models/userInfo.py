# coding: utf-8
from application import db
from common.models.serializer import Serializer


class Userinfo(db.Model):
    __tablename__ = 'userinfo'

    userInfoId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(1024))
    pm = db.Column(db.String(255))
    likeNum = db.Column(db.Integer)
    followNum = db.Column(db.Integer)
    age = db.Column(db.Integer)
    constellation = db.Column(db.String(16))
    movieTags = db.Column(db.String(64))

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d