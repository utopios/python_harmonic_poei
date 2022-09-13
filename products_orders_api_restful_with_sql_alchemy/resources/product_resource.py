import decimal
from datetime import date

from flask_restful import Resource, reqparse, fields, marshal_with

from fields.products_fields_dto import resource_products_fields
from services.product_service import ProductService
from utils.generic_encoder import GenericEncoder


class ProductResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Merci d'ajouter un titre valide")
    parser.add_argument("price", type=float, required=True, help="Merci d'ajouter un prix valide")
    parser.add_argument("stock", type=int, required=True, help="Merci d'ajouter un stock valide")


    def __init__(self):
        self.product_service = ProductService()

    @marshal_with(resource_products_fields)
    def post(self):
        data = ProductResource.parser.parse_args()
        try:
            product = self.product_service.add_product(data['title'], data['price'], data['stock'])
            # return GenericEncoder().encode(product)
            # avec marshal_with => pas besoin d'encoder
            return product
        except Exception as err:
            return str(err), 500


    def delete(self, id):
        try:
            return self.product_service.delete_product(id)
        except ValueError as err:
            return str(err), 404

    @marshal_with(resource_products_fields)
    def get(self, id=None):
        if id is None:
            # return GenericEncoder().encode(self.product_service.get_products())
            # avec marshal_with => pas besoin d'encoder
            return self.product_service.get_products()
        else:
            try:
                #return GenericEncoder().encode(self.product_service.get_product_by_id(id))
                # avec marshal_with => pas besoin d'encoder
                return self.product_service.get_product_by_id(id)
            except ValueError as err:
                return str(err), 404

    def put(self, id):
        data = ProductResource.parser.parse_args()
        try:
            return self.product_service.update_product(id,data['title'], data['price'], data['stock'])
        except Exception as err:
            return str(err), 500