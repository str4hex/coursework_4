from dao.movies import MoviesDAO


class MoviesService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_all_movie(self):
        return self.dao.get_all_movie()

    def get_movie(self, mid):
        return self.dao.get_movie(mid)

    def get_status_movies(self, page):
        return self.dao.get_status_movies(page)

    def get_page_movie(self, page):
        return self.dao.get_page_movie(page)