from flask import request
from flask_restful import Resource
from flask_injector import inject

from models.simple_user import SimpleUser
from services.simple_service import SimpleService


class SimpleUserResource(Resource):

    ###inject permet d'indiquer de créer les objets à partir de flask-injector
    @inject
    def __init__(self, service:SimpleService):
        self.service = service
    def get(self, email):
        return SimpleUser.find_by_email(email).json()

    def post(self):
        email = request.json.get("email")
        return self.service.add(email)
