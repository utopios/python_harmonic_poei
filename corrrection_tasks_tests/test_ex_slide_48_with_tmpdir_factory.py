import pytest

from init import *

@pytest.fixture(scope='class', autouse=True)
def setup_db(tmpdir_factory):
    folder = tmpdir_factory.mktemp("tmp")
    tasks.start_tasks_db(str(folder), 'tiny')
    yield
    stop_tasks_db()

@pytest.mark.usefixtures('setup_db')
class TestUpdate():

    def equivalent_class(self, t1, t2, task_id):
        return ((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done) and t2.id == task_id)

    @pytest.mark.parametrize("method", [tasks.add, tasks.update])
    def test_add_not_task_raises(self, method):
        """add() should raise an exception if wrong type instance"""
        with pytest.raises(TypeError):
            method(task='not task')

    def test_update_correct_task(self):
        """tasks. update(<valid_id>, new task value) should update task"""
        # Arrange
        new_task = Task("new task", done=False)
        task_id = tasks.add(new_task)

        # Act
        new_value_task = Task("new value task", done=True)
        tasks.update(task_id, new_value_task)
        compare_task = tasks.get(task_id)

        assert self.equivalent_class(new_value_task, compare_task, task_id)
