from json import JSONEncoder


class GenericEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__