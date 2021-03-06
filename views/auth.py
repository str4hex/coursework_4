from flask import request
from container import user_service, auth_service
from flask_restx import Resource, Namespace

ns_auth = Namespace('auth')


@ns_auth.route('/register/')
class UserCreateView(Resource):

    def post(self):
        user_data = request.json
        user_service.create_user(user_data)
        return '', 204



@ns_auth.route('/login/')
class UserViews(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')
        if not (email or password):
            return "Не задано имя или пароль", 400

        tokens = auth_service.generate_token(email,password)
        if tokens:
            return tokens, 202
        else:
            return "Ошибка в запросе", 400

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if not refresh_token:
            return "Не задан токен", 400

        tokens = auth_service.refresh_token(refresh_token)
        if tokens:
            return tokens
        else:
            return "Ошибка в запросе", 400




