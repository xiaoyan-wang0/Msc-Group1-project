# coding: utf-8
from application import db
from common.models.serializer import Serializer

#database
class User(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64, 'utf8mb4_0900_ai_ci'))
    email = db.Column(db.String(64, 'utf8mb4_0900_ai_ci'))
    password = db.Column(db.String(255))
    ifBlocked = db.Column(db.Integer)
    #createTime = db.Column(db.DateTime, server_default=db.FetchedValue())

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d