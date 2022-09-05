import pytest

from init import *


@pytest.mark.xfail
def test_unique_id_is_a_duck():
    """Demonstrate xfail."""
    initialized_tasks_db()
    uid = tasks.unique_id()
    stop_tasks_db()
    assert uid == 'a duck'


@pytest.mark.xfail(tasks.__version__ < '1.2', reason='not supported until version 1.2')
def test_unique_id_1():
    """Demonstrate xfail wth tasks version"""
    initialized_tasks_db()
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    stop_tasks_db()
    assert id_1 != id_2