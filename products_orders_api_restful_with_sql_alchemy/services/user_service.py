from flask_injector import inject
from flask_jwt_extended import create_access_token

from models.user import User
from repositories.genric_repository import GenericRepository
from repositories.user_repository import UserRepository


class UserService:

    @inject
    def __init__(self, repository:UserRepository):
        self.repository = repository


    def save_user(self, email, password, role):
        user = User(email, password, role)
        return self.repository.save(user)

    def login_user(self, email, password):
        user = self.repository.find_user_by_email(email)
        if user is not None:
            ##Check hash password
            if user.password == password:
                ###Create token
                token = create_access_token(user.email, additional_claims={'role': user.role})
                return token
                pass
        else:
            return {"message": "wrong user or password"}, 401
