from injector import inject

from models.simple_user import SimpleUser
from repository.repository import Repository


class SimpleService:

    @inject
    def __init__(self, repository:Repository):
        self.repository = repository

    def add(self, email):
        u = SimpleUser(email)
        # u.save_to_db()
        return self.repository.add(u).json()