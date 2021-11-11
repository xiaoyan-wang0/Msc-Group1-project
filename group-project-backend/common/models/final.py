# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from common.models.serializer import Serializer

db = SQLAlchemy()



class Final(db.Model):
    __tablename__ = 'final'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    movieId = db.Column(db.Integer)
    overview = db.Column(db.String(1080))
    genre_ids = db.Column(db.String(32))

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d