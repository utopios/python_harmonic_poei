import pytest

from init import *


@pytest.fixture(name="few_tasks", params=(
        Task("Sample Task"),
        Task("Second one"),
        Task("Last one")
    ))
def just_a_few_tasks(request):
    """create fex tasks"""
    return request.param

@pytest.fixture(autouse=True)
def start_db():
    initialized_tasks_db()

@pytest.fixture
def add_tasks_fixture(few_tasks):
    count = tasks.count()
    tasks.add(few_tasks)
    return count


def test_add_with_multiple_fixture(add_tasks_fixture):
    ###Ce test est appelé 3 fois car la fixutre add_tasks_fixture utilise une fixture params
    task = Task("More task")
    tasks.add(task)
    count = tasks.count()
    stop_tasks_db()
    assert count == add_tasks_fixture + 2