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


@tasks_controller.get("/")
def listar_tasks():
    tasks = service.listar()
    return [
        {
            "id": str(t.id),
            "titulo": t.titulo,
            "descricao": t.descricao,
            "concluida": t.concluida
        }
        for t in tasks
    ]


@tasks_controller.get("/{task_id}")
def obter_task(task_id: UUID):
    try:
        task = service.obter(task_id)
        return {
            "id": str(task.id),
            "titulo": task.titulo,
            "descricao": task.descricao,
            "concluida": task.concluida
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@tasks_controller.delete("/{task_id}")
def deletar_task(task_id: UUID):
    try:
        service.remover(task_id)
        return {"mensagem": "Tarefa removida"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))