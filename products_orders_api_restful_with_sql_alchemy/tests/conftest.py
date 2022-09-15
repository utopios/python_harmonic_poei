import pytest

from utils.app_factory import create_app


@pytest.fixture(scope='session')
def get_app():
    return create_app({'MODE': 'TEST'})

@pytest.fixture(scope='session')
def client(get_app):
    with get_app.test_client() as c:
        yield c


@pytest.fixture(scope='session')
def get_jwt(client):
    response = client.post('/users/login', json={'email': 'ihab@utopios.net', 'password':'123456789'})
    return response.json