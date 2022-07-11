from flask_restx import Resource, Namespace
from dao.models.genre import GenreSchema
from container import genres_service

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()

ns_genres = Namespace('genres')


@ns_genres.route('/')
class GenresViews(Resource):

    def get(self):
        all_movies = genres_service.get_all_genres()
        return genres_schema.dump(all_movies), 200

@ns_genres.route('/<int:gid>')
class GenreViews(Resource):

    def get(self, gid):
        movie = genres_service.get_genre(gid)
        return genre_schema.dump(movie), 200