class TaskRepository:
    def __init__(self):
        self._tasks = []

    def adicionar(self, task):
        self._tasks.append(task)


    def obter_por_id(self, task_id):
        return next((t for t in self._tasks if t.id == task_id), None)


    def listar(self):
        return self._tasks
    

    def remover(self, task_id):
        self._tasks = [t for t in self._tasks if t.id != task_id]