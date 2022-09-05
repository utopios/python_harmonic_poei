from init import *
import pytest


class TestExcpetions():

    @pytest.mark.parametrize("method",[tasks.add, tasks.update])
    def test_add_not_task_raises(self, method):
        """add() should raise an exception if wrong type instance"""
        with pytest.raises(TypeError):
            method(task='not task')

    def test_add_wrong_owner_raises(self):
        """add() should raise an exception if wrong type instance"""
        with pytest.raises(ValueError):
            tasks.add(Task("simple task", owner=1))

    def test_add_none_db_raises(self):
        with pytest.raises(tasks.UninitializedDatabase):
            tasks.add(Task("simple task"))