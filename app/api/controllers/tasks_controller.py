from application.services.tasks_services import TaskService
from infrastructure.repositories.tasks_repository import TaskRepository
from fastapi import APIRouter, HTTPException
from uuid import UUID

# Instanciando (simples, sem DI container)
tasks_controller = APIRouter(prefix="/tasks", tags=["Usuario"])
repo = TaskRepository()
service = TaskService()


@tasks_controller.post("/")
def criar_task(titulo: str, descricao: str):
    task = service.criar(titulo, descricao)
    return {
        "id": str(task.id),
        "titulo": task.titulo,
        "descricao": task.descricao,
        "concluida": task.concluida
    }