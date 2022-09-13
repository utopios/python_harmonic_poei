from flask import Flask
from flask_restful import Api

from resources.order_resource import OrderResource
from resources.product_resource import ProductResource
from utils.config import postgresql_string

app = Flask(__name__)

##Ajouter la configuration postgres à notre app
app.config['SQLALCHEMY_DATABASE_URI'] =postgresql_string

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
