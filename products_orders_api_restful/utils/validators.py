from services.product_service import ProductService


class Validators:

    @staticmethod
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