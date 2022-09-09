class TodosList:
    count = 0

    def __init__(self, title):
        TodosList.count += 1
        self.id = TodosList.count
        self.title = title
        self.items = []

    def add_item(self, todo_item):
        self.items.append(todo_item)
