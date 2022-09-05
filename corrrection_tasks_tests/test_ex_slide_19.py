import pytest

from init import *


@pytest.mark.parametrize("task",
                         [Task('task1', done=True),
                          Task('task2', 'me'),
                          Task('task3', 'Toto', False)]
                         )
def test_add(task):
    """Demo using parametrize mark with one parameter"""
    # Arrange
    initialized_tasks_db()

    # Act
    ##Add Task to Db
    task_id = tasks.add(task)
    ##Get task from db with inserted id
    task_from_db = tasks.get(task_id)
    stop_tasks_db()
    # Assert
    assert equivalent(task, task_from_db, task_id)
