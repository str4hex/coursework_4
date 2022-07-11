from flask_restx import Resource, Namespace
from container import movies_service
from dao.models.movie import MovieSchema

movies_shema = MovieSchema(many=True)
movie_shema = MovieSchema()

ns_movies = Namespace('movies')



@ns_movies.route('/')
class MoviesVies(Resource):

    def get(self):
        get_all_movies = movies_service.get_all_movie()
        return movie_shema.dump(get_all_movies), 200

@ns_movies.route('/<int:mid>')
class MovieVies(Resource):

    def get(self, mid):
        get_movie = movies_service.get_movie(mid)
        return movie_shema.dump(get_movie), 200