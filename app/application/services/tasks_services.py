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