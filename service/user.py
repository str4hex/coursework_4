import base64
import hashlib
import hmac

from const import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO



class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create_user(self, data):
        data['password'] = self.get_password_hash(data.get('password'))
        return self.dao.create_user(data)

    def update_user(self,user_mail, data):
        return self.dao.update_user(user_mail, data)

    def get_user(self, email):
        return self.dao.get_user(email)

    def get_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password, password_hash):
        return hmac.compare_digest(self.get_password_hash(password), password_hash)

    def get_new_password(self, password, email):
        return self.dao.get_new_password(password,email)

