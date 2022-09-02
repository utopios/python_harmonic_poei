import pytest

@pytest.mark.parametrize("p1,p2", [(1, 2), (2, 4), (2, 5)])
def test_double(p1, p2):
    assert p1 * 2 == p2
