from flask import Flask
from flask_restx import Api
from config import Config
from database import db
from views.movies import ns_movies
from views.genres import ns_genres
from views.directors import ns_directors

def application(config):
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def create_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(ns_movies)
    api.add_namespace(ns_genres)
    api.add_namespace(ns_directors)


app = application(Config())
create_app(app)

if __name__ == '__main__':
    app.run()
