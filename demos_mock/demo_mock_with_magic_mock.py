from unittest.mock import Mock

from api_module import CallApi



###TEST######
from demos_mock.function_to_test import get_user_from_api
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
def test_function_with_api_call():
    ###Arrange
    user = "toto"
    ##Création de l'objet à mock
    api = CallApi()

    ###On utilise MagicMock de unitest pour faire le mock de notre api
    api.get_user_with_magic_mock = MagicMock(return_value="{name: 'toto'}")

    ###Act
    ##Utilise mon objet dans la fonction à tester
    get_user_from_api(user, api)

    ###Assert
    with open("user.txt", "r") as f:
        assert f.read() ==  "{name: 'toto'}"