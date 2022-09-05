import pytest


def inc(x):
    return x + 1

condition = 11

@pytest.mark.xfail
def test_answer_fail():
    assert inc(3) == 6

@pytest.mark.xfail(condition > 10, strict=True, reason="xfail when condition gt 10")
def test_answer_success():
    assert inc(3) == 4