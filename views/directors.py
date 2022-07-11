from flask_restx import Resource, Namespace
from container import directors_service
from dao.models.director import DirectorSchema

directors_shema = DirectorSchema(many=True)
director_shema = DirectorSchema()


ns_directors = Namespace('directors')


@ns_directors.route('/')
class DirectorsVires(Resource):

    def get(self):
        all_directors = directors_service.get_all_directors()
        return directors_shema.dump(all_directors)

@ns_directors.route('/<int:did>')
class DirectorsVires(Resource):

    def get(self,did):
        director =  directors_service.get_directors(did)
        return director_shema.dump(director)