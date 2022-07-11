from sqlalchemy import desc

from dao.models.movie import Movie


class MoviesDAO:

    def __init__(self, session):
        self.session = session

    def get_all_movie(self):
        return self.session.query(Movie).all()

    def get_movie(self, mid):
        return self.session.query(Movie).get(mid)

    def get_page_movie(self, page):
        return self.session.query(Movie).paginate(page=page, per_page=12)

    def get_status_movies(self, page):
        return self.session.query(Movie).order_by(desc(Movie.year)).paginate(page=page, per_page=12)
