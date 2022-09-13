import threading

from models.order import Order
from models.product import Product


class OrderService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(OrderService, cls).__new__(cls)
                    cls._instance.orders = []
        return cls._instance

    ##Version avec generateur
    def _find(self,id):
        try:
            return next(o for o in self.orders if o.id == id)
        except:
            raise ValueError("order not found")

    def add_order(self, products):
        try:
            order = Order()
            for p in products:
                order.add_product(p)
            self.orders.append(order)
            return order
        except:
            raise Exception("Error when adding product")


    def get_orders(self):
        return self.orders

    def get_order_by_id(self, id):
        try:
            order = self._find(id)
            return order
        except ValueError as err:
            raise err