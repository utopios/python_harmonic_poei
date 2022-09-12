
class Product:
    count = 0

    def __init__(self, title, price, stock):
        Product.count += 1
        self.id = Product.count
        self.title = title
        self.price = price
        self.stock = stock
