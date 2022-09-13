from flask import request
from flask_restful import Resource

from models.simple_user import SimpleUser


class SimpleUserResource(Resource):

    def get(self, email):
        return SimpleUser.find_by_email(email).json()

    def post(self):
        email = request.json.get("email")
        u = SimpleUser(email)
        u.save_to_db()
        return u.json()
