import calendar
import datetime
import hmac
import jwt

from const import JWT_SECRET_KEY
from dao.user import UserDAO
from service.user import UserService


class AuthService:

    def __init__(self, dao: UserDAO, service: UserService):
        self.dao = dao
        self.service = service

    def generate_token(self, email, password, is_refresh=False):
        user_email = self.dao.get_user(email)

        if not email:
            return False

        if not is_refresh:
            if not self.compare_password(password, user_email.password):
                return False



        data = {"email": email}


        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET_KEY, algorithm='HS256')


        days = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data["exp"] = calendar.timegm(days.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET_KEY, algorithm='HS256')


        return {"access_token": access_token, 'refresh_token': refresh_token}

    def compare_password(self, password, password_hash):
        return hmac.compare_digest(self.service.get_password_hash(password), password_hash)
