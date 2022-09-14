from flask import Flask
from flask_injector import request, FlaskInjector
from flask_restful import Api

from database import db
from repository.repository import Repository
from resources.simple_user_resource import SimpleUserResource
from services.simple_service import SimpleService


def app_factory(config):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE_URI"]
    app.config["DEBUG"] = config["MODE"]
    api = Api(app)

    @app.before_first_request
    def initialisation():
        db.init_app(app)
        ##Création des tables
        db.create_all()

    api.add_resource(SimpleUserResource, '/simple', '/simple/<string:email>', endpoint='simple')

    def configure(binder):
        if config["MODE"] == "DEBUG":
            ##Le scope peut être request ou singleton
            ##On ajoute dans flaks-injector les service du mode debug ou test
            binder.bind(SimpleService, to=SimpleService, scope=request)
            binder.bind(Repository, to=Repository, scope=request)
        else:
            binder.bind(SimpleService, to=SimpleService, scope=request)
            binder.bind(Repository, to=Repository, scope=request)

    FlaskInjector(app=app, modules=[configure])

    return app
