from database import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.COlumn(db.String, unique=True)
    password = db.COlumn(db.String)
    name = db.COlumn(db.String)
    surname = db.COlumn(db.String)
    favorite_genre = db.COlumn(db.String)


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()
