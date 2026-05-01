from domain.entities.tasks_entity import TasksEntity
from infrastructure.repositories.tasks_repository import TaskRepository
from uuid import UUID
from typing import List

class TaskService:
    def __init__(self):
        self._repo = TaskRepository()


    def criar(self, titulo: str, descricao: str):
        task = TasksEntity(titulo, descricao)
        self._repo.adicionar(task)
        return task
    

    def listar(self) -> List[TasksEntity]:
        return self._repo.listar()

    
    def obter(self, task_id: UUID) -> TasksEntity:
        task = self._repo.obter_por_id(task_id)
        if not task:
            raise Exception("Task não encontrada")
        return task
    

    def remover(self, task_id: UUID):
        task = self.obter(task_id)  # GARANTE EXISTÊNCIA
        self._repo.remover(task.id)