import pytest


@pytest.fixture
def first_fixture():
    return {"first_name": "ihab", "last_name": "abadi"}

@pytest.fixture
def second_fixture(first_fixture):
    first_fixture["email"] = "ihab@utopios.net"
    return first_fixture

def test_fixture_multiple(second_fixture):
    assert second_fixture["first_name"] == 'ihab'
    assert second_fixture["last_name"] == 'abadi'
    assert second_fixture["email"] == 'ihab@utopios.net'