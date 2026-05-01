class TaskRepository:
    def __init__(self):
        self._tasks = []

    def adicionar(self, task):
        self._tasks.append(task)