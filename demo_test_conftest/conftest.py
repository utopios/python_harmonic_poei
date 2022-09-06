import pytest


@pytest.fixture
def input_value():
    return 33

@pytest.hookimpl(hookwrapper=True)
def pytest_collection(session):
    ###Execute instructions before builtin pytest_collection
    yield
    ###Execute instructions after builtin pytest_collection

def pytest_itemcollected(item):
    pass

def pytest_runtest_call(item):
    print(item.name)
    pass