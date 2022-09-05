from init import *
import pytest


class TestExcpetions():

    def test_add_not_task_raises(self):
        """add() should raise an exception if wrong type instance"""
        with pytest.raises(TypeError):
            tasks.add(task='not task')

    def test_add_wrong_owner_raises(self):
        """add() should raise an exception if wrong type instance"""
        with pytest.raises(ValueError):
            tasks.add(Task("simple task", owner=1))

    def test_add_none_db_raises(self):
        with pytest.raises(tasks.UninitializedDatabase):
            tasks.add(Task("simple task"))