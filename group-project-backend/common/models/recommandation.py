# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from common.models.serializer import Serializer

db = SQLAlchemy()



class Recommandation(db.Model):
    __tablename__ = 'recommandation'

    id = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.String(16))
    userId = db.Column(db.Integer)
    createTime = db.Column(db.DateTime, server_default=db.FetchedValue())
    tagId = db.Column(db.Integer)


    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d