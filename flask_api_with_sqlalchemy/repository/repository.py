from database import db


class Repository:

    def __init__(self):
        pass

    def add(self, element):
        db.session.add(element)
        db.session.commit()
        return element