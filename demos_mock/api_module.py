import json

import requests


class CallApi:
    def __init__(self):
        self.user_info = None

    ###Cette méthode a été utilisée avec monckeypatch
    def get_user(self, user):
        result = requests.get('http://localhost/users/' + user)
        self.user_info = json.dump(result.json())

    ###Cette méthode a été utilisée avec magicMock
    def get_user_with_magic_mock(self, user):
        result = requests.get('http://localhost/users/' + user)
        return json.dump(result.json())
