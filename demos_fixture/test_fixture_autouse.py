import pytest


@pytest.fixture
def first_fixture():
    return "test"

@pytest.fixture
def second_fixture(first_fixture):
    return []

@pytest.fixture(autouse=True)
def autouse_fixture(first_fixture, second_fixture):
    second_fixture.append(first_fixture)


def test_with_auto_use(first_fixture, second_fixture):
    assert second_fixture == [first_fixture]