from flask import Flask
from flask_injector import request, FlaskInjector
from flask_jwt_extended import JWTManager
from flask_restful import Api

from database import db
from repository.mock_repository import MockRepository
from repository.repository import Repository
from resources.jwt_resource import JwtResource
from resources.simple_user_resource import SimpleUserResource
from services.identification_service import IdentificationService
from services.simple_service import SimpleService


def app_factory(config):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE_URI"]
    app.config["DEBUG"] = config["MODE"]
    api = Api(app)

    ##Pour créer un jwt à l'aide de la librairie flask-jwt-extended, on crée un objet JWTManager
    app.config["JWT_SECRET_KEY"] = "je suis la clé de sécurité pour générer le jwt"
    jwt_manager = JWTManager(app)
    @app.before_first_request
    def initialisation():
        db.init_app(app)
        ##Création des tables
        db.create_all()

    api.add_resource(SimpleUserResource, '/simple', '/simple/<string:email>', endpoint='simple')
    api.add_resource(JwtResource, '/jwt', endpoint='jwt')

    def configure(binder):
        if config["MODE"] == "DEBUG":
            ##Le scope peut être request ou singleton
            ##On ajoute dans flaks-injector les service du mode debug ou test
            binder.bind(Repository, to=MockRepository, scope=request)
        else:
            binder.bind(Repository, to=Repository, scope=request)

        binder.bind(SimpleService, to=SimpleService, scope=request)
        binder.bind(IdentificationService, to=IdentificationService, scope=request)

    FlaskInjector(app=app, modules=[configure])

    return app
