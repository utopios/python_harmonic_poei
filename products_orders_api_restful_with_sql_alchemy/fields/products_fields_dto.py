##Les champs à garder dans les réponses sous format dto => data transfer object
from flask_restful import fields
resource_products_fields = {
    "title": fields.String,
    "price": fields.Float,
    "id": fields.Integer
    # "url": fields.Url('products')
}