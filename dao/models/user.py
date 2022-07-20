from database import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favourite_genre = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()
