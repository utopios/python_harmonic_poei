from models.product import Product


class ProductService:

    #products = []
    def __init__(self):
        self.products = []

    # @staticmethod
    # def _find(id):
    #     product = None
    #     for t in products:
    #         if t.id == id:
    #             todolist = t
    #             break
    #     pass
    ##ou
    ##non static

    # def _find(self,id):
    #     product = None
    #     for t in self.products:
    #         if t.id == id:
    #             todolist = t
    #             break
    #     return product

    ##Version avec generateur
    def _find(self,id):
        try:
            return next(p for p in self.products if p.id == id)
        except:
            raise ValueError("product not found")

    def add_product(self, title, price, stock):
        try:
            product = Product(title, price, stock)
            self.products.append(product)
            return product
        except:
            raise Exception("Error when adding product")

    def delete_product(self, id):
        try:
            product = self._find(id)
            self.products.remove(product)
            return True
        except ValueError as err:
            raise err


    def get_products(self):
        return self.products

    def get_product_by_id(self, id):
        try:
            product = self._find(id)
            return product
        except ValueError as err:
            raise err