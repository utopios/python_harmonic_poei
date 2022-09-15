from flask_restful import Resource, reqparse, marshal_with
from flask_injector import inject

from fields.users_fields_dto import resource_users_fields
from services.user_service import UserService


class UserResource(Resource):

    @inject
    def __init__(self, service: UserService):
        self.user_service = service

    ##Creation d'un parser pour extraire les données de la request
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str,required=True, help='Email for user cannot be blank')
    parser.add_argument('password', type=str,required=True, help='password for user cannot be blank')
    parser.add_argument('role', type=str,required=True, help='role for user cannot be blank')
    ##Enregistrer un user
    @marshal_with(resource_users_fields)
    def post(self):
        """
               Create a new user
               ---
               tags:
                 - users
                 - user
               parameters:
                 - in: body
                   name: body
                   schema:
                     id: User
                     required:
                       - email
                       - password
                       - role
                     properties:
                       email:
                         type: string
                         description: email for user
                       password:
                         type: string
                         description: name for user
                       role:
                         type: string
                         description: role for user
               responses:
                 200:
                   description: User created
               """
        data = UserResource.parser.parse_args()
        return self.user_service.save_user(data["email"], data["password"], data["role"])