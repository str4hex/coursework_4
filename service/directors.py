from dao.directors import DirectorsDAO


class DirectorsService:

    def __init__(self, dao: DirectorsDAO):
        self.dao = dao

    def get_all_directors(self):
        return self.dao.get_all_directors()  

    def get_directors(self, did):
        return self.dao.get_directors(did)