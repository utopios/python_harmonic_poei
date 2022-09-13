from datetime import datetime

from utils.database import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)

    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock
        self.created_date = datetime.now()
        self.updated_date = datetime.now()

    def json(self):
        return {'title': self.title, 'price': self.price, 'created_date': self.created_date.strftime('%d-%m-%Y %H:%I:%S')}
