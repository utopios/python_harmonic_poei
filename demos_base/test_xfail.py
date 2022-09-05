import pytest


def inc(x):
    return x + 1

condition = False

@pytest.mark.xfail
def test_answer_fail():
    assert inc(3) == 6

@pytest.mark.xfail(condition, strict=True)
def test_answer_success():
    assert inc(3) == 4