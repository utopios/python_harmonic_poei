from flask_restful import fields

from fields.products_fields_dto import resource_products_fields

resource_orders_fields = {
    "id": fields.Integer,
    "products": fields.List(fields.Nested(resource_products_fields)),
    "url": fields.Url('orders')
}