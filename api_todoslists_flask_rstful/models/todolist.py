class TodoList:
    count = 0

    def __init__(self, title):
        TodoList.count += 1
        self.id = TodoList.count
        self.title = title
        self.items = []

    def add_item(self, todo_item):
        self.items.append(todo_item)