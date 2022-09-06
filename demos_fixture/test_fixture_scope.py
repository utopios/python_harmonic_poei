import pytest

count_fixture_run = 0
@pytest.fixture(scope="session")
def input_value():
    global count_fixture_run
    count_fixture_run = count_fixture_run + 1
    return 33


def test_div_by_11(input_value):
    assert input_value % 11 == 0


def test_div_by_3(input_value):
    assert input_value % 3 == 0