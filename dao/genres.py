from dao.models.genre import Genre


class GenresDAO:

    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_genre(self, gid):
        return self.session.query(Genre).get(gid)
