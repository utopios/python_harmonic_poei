import pytest

from init import *

class Meta(type):
    def __call__(self, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        custom_init = getattr(instance, "__custom_init__", None)
        if callable(custom_init):
            custom_init(*args, **kwargs)

        return instance

@pytest.mark.smoke
class TestUpdate(metaclass=Meta):
    def __custom_init__(self):
        initialized_tasks_db()

    # def __init__(self):
    #     initialized_tasks_db()

    # def __new__(cls, *args, **kwargs):
    #     return

    def equivalent_class(self, t1, t2, task_id):
        return ((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done) and t2.id == task_id)

    def test_update_correct_task(self):
        """tasks. update(<valid_id>, new task value) should update task"""
        # Arrange
        #initialized_tasks_db()
        new_task = Task("new task", done=False)
        task_id = tasks.add(new_task)

        # Act
        new_value_task = Task("new value task", done=True)
        tasks.update(task_id, new_value_task)
        compare_task = tasks.get(task_id)
        stop_tasks_db()

        assert self.equivalent_class(new_value_task, compare_task, task_id)
