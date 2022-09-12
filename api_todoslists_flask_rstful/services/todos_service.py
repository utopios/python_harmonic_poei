from models.todoitem import TodoItem
from models.todolist import TodoList
import threading

###Implémentation du singleton thread safe
class TodosService:
    _instance = None
    ##Lock pour le thread safe
    _lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if  cls._instance is None:
                    cls._instance = super(TodosService, cls).__new__(cls)
                    cls._instance.todos_lists = []
        return cls._instance



    def add_todo_list(self, title):
        todoslist = TodoList(title)
        self.todos_lists.append(todoslist)
        return todoslist

    def delete_todo_list(self, id):
        todolist = None
        for t in self.todos_lists:
            if t.id == id:
                todolist = t
                break
        if todolist is not None:
            self.todos_lists.remove(todolist)
            return True
        raise ValueError("No todolist with this id")


    def get_todo_list(self, id):
        todolist = None
        for t in self.todos_lists:
            if t.id == id:
                todolist = t
                break

        if todolist is not None:
            return todolist
        raise ValueError("No todolist with this id")

    def add_todoitem_to_todos_list(self, todolist_id, task_name):
        todolist = None
        for t in self.todos_lists:
            if t.id == todolist_id:
                todolist = t
                break
        if todolist is None:
            raise ValueError("No todolist with this id")
        todoitem = TodoItem(task_name)
        todolist.add_item(todoitem)
        return todoitem

    def delete_todoitem_from_todos_list(self, todolist_id, todoitem_id):
        todolist = None
        todoitem = None
        for t in self.todos_lists:
            if t.id == todolist_id:
                todolist = t
                break
        if todolist is None:
            raise ValueError("No todolist with this id")
        for item in todolist.items:
            if item.id == todoitem_id:
                todoitem = item
                break
        if todoitem is None:
            raise ValueError("No todoitem with this id")
        todolist.items.remove(todoitem)
        return True