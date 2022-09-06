import pytest

db = None

@pytest.fixture
def fixture_yield():
    global db
    db = True
    yield
    db = False
    print(db)


def test_with_fixture_yield(fixture_yield):
    assert db == True

