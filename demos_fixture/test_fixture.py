import pytest


@pytest.fixture
def input_value():
    return 33


def test_div_by_11(input_value):
    assert input_value % 11 == 0


def test_div_by_3(input_value):
    assert input_value % 3 == 0