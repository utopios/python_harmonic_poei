

from flask_restful import Resource, reqparse

from services.order_service import OrderService
from services.product_service import ProductService
from utils.generic_encoder import GenericEncoder

##value est la valeur envoyée par l'utilisateur de l'api => dans ce cas value est une liste de products id
def products_validator(value):
    ##services product service pour vérifier et chercher les produits dans notre base de données
    product_service = ProductService()
    products = []
    for id in value:
        try:
            product = product_service.get_product_by_id(id)
            products.append(product)
        except ValueError as err:
            raise err
    return products

class OrderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("products", type=products_validator, required=True, help="Merci d'ajouter les ids des produits")

    def __init__(self):
        self.order_service = OrderService()

    def post(self):
        data = OrderResource.parser.parse_args()
        try:
            order = self.order_service.add_order(data)
            return GenericEncoder().encode(order)
        except Exception as err:
            return str(err), 500

    def get(self, id=None):
        if id is not None:
            return GenericEncoder().encode(self.order_service.get_orders())
        else:
            try:
                return GenericEncoder().encode(self.order_service.get_order_by_id(id))
            except ValueError as err:
                return str(err), 404
