from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

##En utilisant l'objet config d'une application flask, on peut ajouter les informations nécessaires à SQLALCHEMY
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cours:db@localhost/harmonic"

#Ajoute un middleware à notre app => un middelware va prendre l'application flask comme paramètre pour
# lui ajouter des nouvelles fonctionnalités, telque la gestion des ressources avec flask_restful, et
# une db avec flask-sqlalchemy

api = Api(app)

db = SQLAlchemy(app)

##création model
class SimpleUser(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    __tablename__ = 'simple_user'

##Création des tables

db.create_all()


if __name__ == '__main__':
    app.run()
