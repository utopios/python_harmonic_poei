from json import JSONEncoder

class PersonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name + " " + self.last_name
