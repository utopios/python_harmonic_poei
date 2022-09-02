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
    #Arrange
    initialized_tasks_db()
    task = Task("do something")
    #Act
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    stop_tasks_db()
    #assert
    assert task_from_db.id == task_id

def test_unique_id_1():
    """Calling unique_id() twice should return different numbers"""
    initialized_tasks_db()
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

def test_unique_id_2():
    """unique_id() should return an unused id"""
    ids = []
    initialized_tasks_db()
    ids.append(tasks.add(Task("first")))
    ids.append(tasks.add(Task("second")))

    uid = tasks.unique_id()
    stop_tasks_db()
    assert uid not in ids

def initialized_tasks_db():
    tasks.start_tasks_db(str('temp'), 'tiny')

def stop_tasks_db():
    tasks.stop_tasks_db()
