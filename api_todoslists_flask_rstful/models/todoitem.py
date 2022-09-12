class TodoItem:
    count = 0

    def __init__(self, task_name):
        TodoItem.count += 1
        self.id = TodoItem.count
        self.task_name = task_name