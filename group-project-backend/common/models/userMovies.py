# coding: utf-8
from application import db
from common.models.serializer import Serializer


class Usermovy(db.Model):
    __tablename__ = 'usermovies'

    Id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    moiveId = db.Column(db.Integer)
    type = db.Column(db.Integer)
    createTime = db.Column(db.DateTime, server_default=db.FetchedValue())

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d
