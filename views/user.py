from flask import request, abort
from flask_restx import Resource, Namespace
import jwt

from container import user_service
from const import JWT_SECRET_KEY
from dao.models.user import UserSchema

ns_user = Namespace('user')
user_shema = UserSchema()


@ns_user.route('/')
class ViewUser(Resource):

    def get(self):

        if not "Authorization" in request.headers:
            abort(401)

        token = request.headers['Authorization'].split()

        try:
            data = jwt.decode(token[1], JWT_SECRET_KEY, algorithms="HS256")
        except Exception as e:
            print(f"JWT decode error{e}")
            abort(401)

        user = user_service.get_user(data['email'])

        return user_shema.dump(user)
