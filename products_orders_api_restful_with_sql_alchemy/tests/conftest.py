import pytest

from utils.app_factory import create_app


@pytest.fixture
def get_app():
    return create_app({'MODE': 'TEST'})

@pytest.fixture
def client(get_app):
    with get_app.test_client() as c:
        yield c