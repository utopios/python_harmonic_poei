class Order:
    count = 0

    def __init__(self):
        Order.count += 1
        self.id = Order.count
        self.products = []

    @property
    def total(self):
        total = 0
        for p in self.products:
            total += p.price
        return total

    def add_product(self, product):
        self.products.append(product)