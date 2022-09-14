from flask import Flask
from flask_injector import FlaskInjector, request
from flask_restful import Api

from repositories.genric_repository import GenericRepository
from resources.order_resource import OrderResource
from resources.product_resource import ProductResource
from services.product_service import ProductService
from utils.config import postgresql_string, postgresql_string_test


def create_app(config):


    app = Flask(__name__)

    ##Ajouter la configuration postgres à notre app
    if config["MODE"] == "TEST":
        app.config['SQLALCHEMY_DATABASE_URI'] =postgresql_string_test
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_string

    ##Création de l'api et l'ajout des ressources, Api de flask restful est un middleware (A avoir dans en detail dans la prtie sécurité)
    api = Api(app)

    @app.before_first_request
    def initialize_db():
        from utils.database import db
        db.init_app(app)
        db.create_all()

    ##ressources product
    api.add_resource(ProductResource, '/products', '/products/<int:id>', endpoint='products')
    api.add_resource(OrderResource, '/orders', '/orders/<int:id>', endpoint='orders')

    def flask_injector_configuration(binder):
        binder.bind(ProductService, to=ProductService, scope=request)
        binder.bind(GenericRepository, to=GenericRepository, scope=request)

    FlaskInjector(app=app, modules=[flask_injector_configuration])
    return app