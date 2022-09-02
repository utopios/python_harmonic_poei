from init import *

def test_add_task_returns_valid_id():
    """tasks.add(<valid task>) should return an integer"""
    #Arrange
    #start tasks db
    initialized_tasks_db()
    task = Task("do something")
    #Act
    task_id = tasks.add(task)
    stop_tasks_db()
    #Assert
    assert isinstance(task_id, int)

def test_added_task_has_id_set():
    """Be sure that the task_id field is set in database by taks.add()"""
    #Arange
    initialized_tasks_db()
    task = Task("do something")
    #Act
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    #assert
    assert task_from_db.id == task_id

def initialized_tasks_db():
    tasks.start_tasks_db(str('temp'), 'tiny')

def stop_tasks_db():
    tasks.stop_tasks_db()
