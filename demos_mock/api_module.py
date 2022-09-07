import json

import requests


class CallApi:
    def __init__(self):
        self.user_info = None
    def get_user(self, user):
        result = requests.get('http://localhost/users/' + user)
        self.user_info = json.dump(result.json())
