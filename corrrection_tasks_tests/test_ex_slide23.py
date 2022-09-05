import pytest

from init import *

@pytest.mark.skip(reason= "misunderstood api")
def test_unique_id_1():
    initialized_tasks_db()
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    stop_tasks_db()
    assert id_1 != id_2