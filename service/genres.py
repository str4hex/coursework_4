from dao.genres import GenresDAO

class GenresService:
    def __init__(self, dao: GenresDAO):
        self.dao = dao

    def get_all_genres(self):
        return self.dao.get_all_genres()

    def get_genre(self, gid):
        return self.dao.get_genre(gid)