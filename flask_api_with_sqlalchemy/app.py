from flask import Flask
from flask_injector import FlaskInjector, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from injector import singleton

from app_factory import app_factory
from database import db
from repository.mock_repository import MockRepository
from repository.repository import Repository
from resources.simple_user_resource import SimpleUserResource
from services.simple_service import SimpleService

# app = Flask(__name__)
#
# ##En utilisant l'objet config d'une application flask, on peut ajouter les informations nécessaires à SQLALCHEMY
# ######################################################user:password@host/dabase
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cours:db@localhost/harmonic"
# app.config["DEBUG"] = True
# #Ajoute un middleware à notre app => un middelware va prendre l'application flask comme paramètre pour
# # lui ajouter des nouvelles fonctionnalités, telque la gestion des ressources avec flask_restful, et
# # une db avec flask-sqlalchemy
#
# api = Api(app)
#
# ##On peut créer la db dans un module externe, et ajouter à notre app
# #db = SQLAlchemy(app)
#
#
# ##L'initialisation et la création des tables peut se faire uniquement avant la première requete vers notre api
# ##à l'aides des hooks flask
# ##Pour l'ajouter à notre app on peut utiliser init_app de flask-SQLACLHEMY
# @app.before_first_request
# def initialisation():
#     db.init_app(app)
#     ##Création des tables
#     db.create_all()
#
# ##Pour l'ajout, on peut utiliser la session de flask-alchemy
# # user = SimpleUser("ihab@utopios.net")
# # db.session.add(user)
# # db.session.commit()
#
# api.add_resource(SimpleUserResource, '/simple', '/simple/<string:email>', endpoint='simple')
#
# ###Configurer les dependances
# def configure(binder):
#     ##Le scope peut être request ou singleton
#     binder.bind(SimpleService, to=SimpleService, scope=request)
#     binder.bind(Repository, to=Repository, scope=request)
#     #binder.bind(Repository, to=MockRepository, scope=request)
#
#
# ###Utiliser flask injector pour créer un container de dependance et Inversion de controle
# FlaskInjector(app=app, modules=[configure])

app = app_factory({'MODE': 'PROD', 'DATABASE_URI': 'postgresql://cours:db@localhost/harmonic'})
if __name__ == '__main__':
    app.run()
