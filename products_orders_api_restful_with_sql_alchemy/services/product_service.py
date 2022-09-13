from datetime import datetime
import threading


from models.product import Product
from repositories.genric_repository import GenericRepository


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
                    cls._instance.respository = GenericRepository()
        return cls._instance



    def _find(self,id):
        try:
            return self.respository.find_by_id(Product, id)
        except:
            raise ValueError("product not found")

    def add_product(self, title, price, stock):
        try:
            product = Product(title, price, stock)
            return self.respository.save(product)
        except Exception as err:
            raise err

    def delete_product(self, id):
        pass

    def update_product(self, id, new_title, new_price, new_stock):
        pass

    def get_products(self):
        return self.respository.find_all(Product)

    def get_product_by_id(self, id):
        try:
            return self._find(id)
        except ValueError as err:
            raise err