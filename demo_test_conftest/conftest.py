import pytest


@pytest.fixture
def input_value():
    return 33

def pytest_itemcollected(item):
    pass

def pytest_runtest_call(item):
    print(item.name)
    pass