####DEV######
import json

import requests

from demos_mock.api_module import CallApi

### call api has attr => user_info => setted by get_user method
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
    ###Arrange
    user = "toto"
    api = CallApi()
    monkeypatch.setattr(api, 'user_info', "{name:'toto'}")

    ###Act
    get_user_from_api(user, api)

    ###Assert
    with open("user.txt", "a") as f:
        assert f.read() ==  "{name: 'toto'}"