from datetime import datetime
import threading


from models.product import Product


class ProductService:

    #products = []
    _instance = None
    ##Lock pour le thread safe
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ProductService, cls).__new__(cls)
                    cls._instance.products = []
        return cls._instance

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

    def update_product(self, id, new_title, new_price, new_stock):
        try:
            product = self._find(id)
            product.title = new_title
            product.price = new_price
            product.stock = new_stock
            product.updated_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
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