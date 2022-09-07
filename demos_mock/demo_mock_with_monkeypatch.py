####DEV######
import json

import requests

class CallApi:
    def __init__(self):
        self.user_info = None
    def get_user(self, user):
        result = requests.get('http://localhost/users/' + user)
        self.user_info = json.dump(result.json())

api = CallApi()

def get_user_from_api(user, api):
    ###Get users for api and write user's informations in file
    #result = requests.get('http://localhost/users/'+user)
    with open("user.txt", 'a') as f:
        api.get_user(user)
        f.write(api.user_info)
    pass

###TEST######
def test_function_with_api_call(monkeypatch):
    user = "toto"
    api = CallApi()
    monkeypatch.setattr(api, 'user_info', "{name:'toto'}")
    get_user_from_api(user, api)
    with open("user.txt", "a") as f:
        assert f.read() ==  "{name: 'toto'}"