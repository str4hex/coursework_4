from flask import Flask
from flask_restx import Api
from config import Config
from database import db
from views.auth import ns_auth
from views.movies import ns_movies
from views.genres import ns_genres
from views.directors import ns_directors
from flask_cors import CORS

from views.user import ns_user


def application(config):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app=app)
    return app


def create_app(app):

    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    api.add_namespace(ns_movies)
    api.add_namespace(ns_genres)
    api.add_namespace(ns_directors)
    api.add_namespace(ns_auth)
    api.add_namespace(ns_user)




app = application(Config())
create_app(app)


if __name__ == '__main__':
    app.run()
