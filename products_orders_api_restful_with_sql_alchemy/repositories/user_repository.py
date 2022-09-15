from models.user import User
from repositories.genric_repository import GenericRepository
from utils.database import db


class UserRepository(GenericRepository):

    def find_user_by_email(self, email):
        return db.session.query(User).filter_by(email=email).one_or_none()