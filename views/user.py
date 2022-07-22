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

    def patch(self):
        data = request.json
        token = request.headers['Authorization'].split()

        try:
            token_decode = jwt.decode(token[1], JWT_SECRET_KEY, algorithms="HS256")
        except Exception as e:
            print(f"JWT decode error{e}")
            abort(401)

        user_email = token_decode['email']

        return user_service.update_user(user_email, data), 204

@ns_user.route('/password/')
class UserPasswordViews(Resource):

    def put(self):
        data = request.json
        token = request.headers['Authorization'].split()
        decode_token = jwt.decode(token[1], JWT_SECRET_KEY, algorithms="HS256")
        user = user_service.get_user(decode_token['email'])
        if not user_service.compare_password(data['old_password'], user.password):
            return "Введеный пароль не совпадает с действующим паролем", 400

        user_service.get_new_password(user_service.get_password_hash(data['new_password']), decode_token['email'])

        return '', 200
