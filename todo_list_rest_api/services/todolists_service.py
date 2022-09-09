from models.todos_list import TodosList


class TodosListService:

    def __init__(self):
        self.todos_lists = []

    def add_todo_list(self, title):
        todoslist = TodosList(title)
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