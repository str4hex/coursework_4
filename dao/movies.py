from dao.models.movie import Movie

class MoviesDAO:

    def __init__(self, session):
        self.session = session

    def get_all_movie(self):
        return self.session.query(Movie).all()

    def get_movie(self, mid):
        return self.session.query(Movie).get(mid)