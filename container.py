from dao.movies import MoviesDAO
from service.movies import MoviesService
from database import db
from dao.genres import GenresDAO
from service.genres import GenresService
from dao.directors import DirectorsDAO
from service.directors import DirectorsService
from dao.user import UserDAO
from service.user import UserService
from service.auth import AuthService

movies_dao = MoviesDAO(db.session)
genres_dao = GenresDAO(db.session)
directors_dao = DirectorsDAO(db.session)
user_dao = UserDAO(db.session)

movies_service = MoviesService(movies_dao)
genres_service = GenresService(genres_dao)
directors_service = DirectorsService(directors_dao)
user_service = UserService(user_dao)
auth_service = AuthService(user_dao,user_service)