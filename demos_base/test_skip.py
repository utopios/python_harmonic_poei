import pytest


@pytest.mark.skip(reason="no need to execute this test")
def test_function1():
    pass


condition = 11


@pytest.mark.skipif(condition < 10, reason="require condtion lt 10")
def test_function2():
    pass
