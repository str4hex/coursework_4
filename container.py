from dao.movies import MoviesDAO
from service.movies import MoviesService
from database import db
from dao.genres import GenresDAO
from service.genres import GenresService
from dao.directors import DirectorsDAO
from service.directors import DirectorsService


movies_dao = MoviesDAO(db.session)
genres_dao = GenresDAO(db.session)
directors_dao = DirectorsDAO(db.session)

movies_service = MoviesService(movies_dao)
genres_service = GenresService(genres_dao)
directors_service = DirectorsService(directors_dao)
