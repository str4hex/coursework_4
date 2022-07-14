from flask import request
from container import auth_service
from flask_restx import Resource, Namespace

ns_auth = Namespace('auth')


@ns_auth.route('/register')
class UserCreateView(Resource):

    def post(self):
        user_data = request.json
        auth_service.create_user(user_data)
        return '', 204


@ns_auth.route('/login')
class UserViews(Resource):
    data = request.json
    email = data['email']
    password = data['password']
    if not (email or password):
        return "", 400


