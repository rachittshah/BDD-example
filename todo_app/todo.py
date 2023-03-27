class ToDo:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = False

    def mark_task_complete(self, task):
        if task in self.tasks:
            self.tasks[task] = True
