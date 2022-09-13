from datetime import datetime



class Product:
    count = 0

    def __init__(self, title, price, stock):
        Product.count += 1
        self.id = Product.count
        self.title = title
        self.price = price
        self.stock = stock
        self.created_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.updated_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
