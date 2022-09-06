import pytest

from init import *

times_used = 0
@pytest.fixture(name="few_tasks")
def just_a_few_tasks():
    """create fex tasks"""
    return (
        Task("Sample Task"),
        Task("Second one"),
        Task("Last one")
    )

@pytest.fixture(scope='session', autouse=True)
def start_db():
    global times_used
    times_used += 1
    initialized_tasks_db()

def test_add_with_fixture(few_tasks):
    # initialized_tasks_db()
    old_count = tasks.count()
    for t in few_tasks:
        tasks.add(t)
    new_count = tasks.count()
    stop_tasks_db()
    assert new_count == old_count + len(few_tasks)

def test_second_with_db_fixture():
    assert True == True