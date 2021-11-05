# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from common.models.serializer import Serializer

db = SQLAlchemy()



class Review(db.Model):
    __tablename__ = 'reviews'

    reviewId = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.String(32, 'utf8mb4_0900_ai_ci'))
    content = db.Column(db.JSON)
    type = db.Column(db.Integer, info='1: tmdb ;  2: Imdb; 3: youtubu; 4: Twitter')
    createTime = db.Column(db.DateTime, server_default=db.FetchedValue())

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d