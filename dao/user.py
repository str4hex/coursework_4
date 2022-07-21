from dao.models.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def create_user(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return ''

    def update_user(self,data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return ''

    def get_user(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_new_password(self, password, email):
        self.session.query(User).filter(User.email == email).update({User.password:password})
        self.session.commit()
        return ''
