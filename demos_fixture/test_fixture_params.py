import pytest

@pytest.fixture(params=range(0,10, 2))
def first_fixture(request):
    return request.param

@pytest.fixture(params=range(1,10, 2))
def second_fixture(request):
    return request.param

def test_fixture_param(first_fixture, second_fixture):
    assert (first_fixture + second_fixture) % 2 == 0