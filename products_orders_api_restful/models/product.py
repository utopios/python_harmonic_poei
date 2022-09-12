
class Product:
    count = 0

    def __init__(self, title, price, stock):
        self.id = ++Product.count
        self.title = title
        self.price = price
        self.stock = stock
