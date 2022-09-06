import pytest

from init import *


@pytest.fixture(name="few_tasks")
def just_a_few_tasks():
    """create fex tasks"""
    return (
        Task("Sample Task"),
        Task("Second one"),
        Task("Last one")
    )

@pytest.fixture(autouse=True)
def start_db():
    initialized_tasks_db()

@pytest.fixture
def add_tasks_fixture(few_tasks, start_db):
    for t in few_tasks:
        tasks.add(t)

def test_add_with_multiple_fixture(add_tasks_fixture):
    task = Task("More task")
    tasks.add(task)
    count = tasks.count()
    stop_tasks_db()
    assert count == 4