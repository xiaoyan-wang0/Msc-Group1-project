# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from common.models.serializer import Serializer

db = SQLAlchemy()



class Usercomment(db.Model):
    __tablename__ = 'usercomments'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    tagId = db.Column(db.Integer)
    comment = db.Column(db.String(1024))
    createTime = db.Column(db.DateTime, server_default=db.FetchedValue())
    movieId = db.Column(db.String(16))
    toxic = db.Column(db.String(16))
    sentiment = db.Column(db.String(16))
    ifReport = db.Column(db.Integer)
    reporterId = db.Column(db.Integer)
    
    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d