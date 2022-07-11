from database import db
from dao.models.director import Director


class DirectorsDAO:

    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_directors(self,did):
        return self.session.query(Director).get(did)