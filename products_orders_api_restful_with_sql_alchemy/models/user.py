from utils.database import db


class User(db.Model):
    __tablename__ = 'users_app'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300))
    password = db.Column(db.String(300))
    role = db.Column(db.String(300))

    def __init__(self,email, password, role):
        self.email = email
        ###Password should be hashed before inserted in database
        self.password = password
        self.role = role

