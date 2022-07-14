from dao.movies import MoviesDAO
from service.movies import MoviesService
from database import db
from dao.genres import GenresDAO
from service.genres import GenresService
from dao.directors import DirectorsDAO
from service.directors import DirectorsService
from dao.auth import UserDAO
from service.auth import UserService

movies_dao = MoviesDAO(db.session)
genres_dao = GenresDAO(db.session)
directors_dao = DirectorsDAO(db.session)
auth_dao = UserDAO(db.session)

movies_service = MoviesService(movies_dao)
genres_service = GenresService(genres_dao)
directors_service = DirectorsService(directors_dao)
auth_service = UserService(auth_dao)
