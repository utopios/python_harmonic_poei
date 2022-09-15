from flask import Flask, jsonify
from flask_injector import FlaskInjector, request
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_swagger import swagger

from repositories.genric_repository import GenericRepository
from repositories.user_repository import UserRepository
from resources.login_resource import LoginResource
from resources.order_resource import OrderResource
from resources.product_resource import ProductResource
from resources.user_resource import UserResource
from services.product_service import ProductService
from services.user_service import UserService
from utils.config import postgresql_string, postgresql_string_test


def create_app(config):


    app = Flask(__name__)

    ##Ajouter la configuration postgres à notre app
    if config["MODE"] == "TEST":
        app.config['SQLALCHEMY_DATABASE_URI'] =postgresql_string_test
        app.config["JWT_SECRET_KEY"] = "une clé secrete pour générer le jwt en mode test"
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_string
        app.config["JWT_SECRET_KEY"] = "une clé secrete pour générer le jwt en mode prod"

    ##Créer notre JWTManager pour notre application
    jwt = JWTManager(app)

    ##Création de l'api et l'ajout des ressources, Api de flask restful est un middleware (A avoir dans en detail dans la prtie sécurité)
    api = Api(app)

    @app.before_first_request
    def initialize_db():
        from utils.database import db
        db.init_app(app)
        db.create_all()

    ##ressources product, order, user, login
    api.add_resource(ProductResource, '/products', '/products/<int:id>', endpoint='products')
    api.add_resource(OrderResource, '/orders', '/orders/<int:id>', endpoint='orders')
    api.add_resource(UserResource, '/users',  endpoint='users')
    api.add_resource(LoginResource, '/users/login',  endpoint='login')

    ##Ajouter une route pour la documentation swagger
    @app.route('/doc')
    def doc():
        return jsonify(swagger(app))
    def flask_injector_configuration(binder):
        binder.bind(ProductService, to=ProductService, scope=request)
        binder.bind(GenericRepository, to=GenericRepository, scope=request)
        binder.bind(UserService, to=UserService, scope=request)
        binder.bind(UserRepository, to=UserRepository, scope=request)

    FlaskInjector(app=app, modules=[flask_injector_configuration])
    return app