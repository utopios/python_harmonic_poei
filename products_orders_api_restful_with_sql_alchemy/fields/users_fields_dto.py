##Les champs à garder dans les réponses sous format dto => data transfer object
from flask_restful import fields
resource_users_fields = {
    "email": fields.String,
    "id": fields.Integer
    # "url": fields.Url('products')
}