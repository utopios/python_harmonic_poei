

from api_module import CallApi



###TEST######
from demos_mock.function_to_test import get_user_from_api


def test_function_with_api_call(monkeypatch):
    ###Arrange
    user = "toto"
    ##Création de l'objet à mock
    api = CallApi()

    ##utiliser monkeypatch pour modifier les attrs de l'objet
    monkeypatch.setattr(api, 'get_user', '')
    monkeypatch.setattr(api, 'user_info', "{name: 'toto'}")

    ###Act
    ##Utilise mon objet dans la fonction à tester
    get_user_from_api(user, api)

    ###Assert
    with open("user.txt", "r") as f:
        assert f.read() ==  "{name: 'toto'}"