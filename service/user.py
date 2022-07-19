import base64
import hashlib

from const import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO



class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create_user(self, data):
        data['password'] = self.get_password_hash(data.get('password'))
        return self.dao.create_user(data)

    def get_user(self, email):
        return self.dao.get_user(email)

    def get_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))
