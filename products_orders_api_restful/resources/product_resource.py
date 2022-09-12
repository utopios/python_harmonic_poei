import decimal

from flask_restful import Resource, reqparse

from services.product_service import ProductService
from utils.generic_encoder import GenericEncoder


class ProductResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Merci d'ajouter un titre valide")
    parser.add_argument("price", type=float, required=True, help="Merci d'ajouter un prix valide")
    parser.add_argument("stock", type=int, required=True, help="Merci d'ajouter un stock valide")


    def __init__(self):
        self.product_service = ProductService()

    def post(self):
        data = ProductResource.parser.parse_args()
        try:
            product = self.product_service.add_product(data['title'], data['price'], data['stock'])
            return GenericEncoder().encode(product)
        except Exception as err:
            return str(err), 500


    def delete(self, id):
        try:
            return self.product_service.delete_product(id)
        except ValueError as err:
            return str(err), 404


    def get(self, id=None):
        if id is None:
            return GenericEncoder().encode(self.product_service.get_products())
        else:
            try:
                return GenericEncoder().encode(self.product_service.get_product_by_id(id))
            except ValueError as err:
                return str(err), 404
