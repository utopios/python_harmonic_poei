from flask import Flask
from flask_restful import Api

from resources.order_resource import OrderResource
from resources.product_resource import ProductResource

app = Flask(__name__)

##Création de l'api et l'ajout des ressources, Api de flask restful est un middleware (A avoir dans en detail dans la prtie sécurité)
api = Api(app)

##ressources product
api.add_resource(ProductResource, '/products', '/products/<int:id>', endpoint='products')
api.add_resource(OrderResource, '/orders', '/orders/<int:id>', endpoint='orders')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
