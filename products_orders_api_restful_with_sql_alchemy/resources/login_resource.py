from flask_restful import Resource, reqparse, marshal_with
from flask_injector import inject

from fields.users_fields_dto import resource_users_fields
from services.user_service import UserService


class LoginResource(Resource):

    @inject
    def __init__(self, service: UserService):
        self.user_service = service

    ##Creation d'un parser pour extraire les données de la request
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str,required=True, help='Email for user cannot be blank')
    parser.add_argument('password', type=str,required=True, help='password for user cannot be blank')
    ##Enregistrer un user
    def post(self):
        data = LoginResource.parser.parse_args()
        return self.user_service.login_user(data["email"], data["password"])