from sqlalchemy import Table

from utils.database import db

association_table = db.Table('order_product',db.Column('id', db.Integer, primary_key=True), db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                             db.Column('product_id', db.Integer, db.ForeignKey('products.id')))

class Order(db.Model):

    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)

    ##Le paramètre lazy aura une action sur le nombre de requête à réaliser pour récupérer
    ##Les entités jointes à notres order
    ##Lazy dynamic executera la requete à l'itération sur les produits
    ##Lay, par defaut est en select(n+1), join,... voir doc lazy

    products = db.relationship('Product', secondary=association_table, backref='orders', lazy='dynamic')
    def __init__(self):
        self.products = []

    @property
    def total(self):
        total = 0
        for p in self.products:
            total += p.price
        return total

    def add_product(self, product):
        self.products.append(product)