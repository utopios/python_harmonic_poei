from utils.database import db

###Classe pour interaction avec sqlalchemy
class GenericRepository:
    def __init__(self):
        pass

    def save(self, element):
        db.session.add(element)
        db.session.commit()
        return element

    def find_all(self, type):
        # return type.query().all()
        return db.session.query(type).all()

    def find_by_id(self, type, id):
        return db.session.query(type).get(id)

    # def filter_one_by(self, type, filter_function):
    #     return db.session.query(type).filter_by(filter_function).first()