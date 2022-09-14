from flask import request
from flask_restful import Resource
from injector import inject

from services.identification_service import IdentificationService


class JwtResource(Resource):

    @inject
    def __init__(self, service:IdentificationService):
        self.service = service

    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        try:
            return self.service.login(email, password)
        except ValueError as err:
            return str(err), 400
