from models.todos_list import TodosList


class TodosListService:

    def __init__(self):
        self.todos_lists = []

    def add_todo_list(self, title):
        todoslist = TodosList(title)
        self.todos_lists.append(todoslist)
        return todoslist