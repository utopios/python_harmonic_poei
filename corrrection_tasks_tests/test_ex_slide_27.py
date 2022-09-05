from init import *
import pytest

# # uniquement pour l'exemple aucune action sur le test
# class Class1:
#     pass
# class Class2:
#     pass
class TestExcpetions():

    # uniquement pour l'exemple aucune action sur le test
    # @pytest.mark.parametrize("Classe", [Class1, Class2])
    # def test_add_not_task_raises(self, Classe):
    #     """add() should raise an exception if wrong type instance"""
    #     with pytest.raises(TypeError):
    #         obj = Classe()


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