from app.domain.entities.enum_prioridade import PrioridadeEnum
from uuid import uuid4, UUID

class TasksEntity:
    def __init__(self, titulo: str, descricao: str, prioridade: int):
        if not titulo:
            raise ValueError("Título não pode ser vazio")
        
        if prioridade not in [p.value for p in PrioridadeEnum]:
            raise ValueError("Prioridade inválida")
        
        self.id: UUID = uuid4()
        self._titulo = titulo
        self._descricao = descricao
        self._prioridade = prioridade
        self._concluida = False

    @property
    def prioridade(self):
        return self._prioridade

    @property
    def titulo(self):
        return self._titulo

    @property
    def descricao(self):
        return self._descricao

    @property
    def concluida(self):
        return self._concluida
    
    def concluir(self):
        if self._concluida:
            raise Exception("Tarefa já está concluída")
        self._concluida = True

    def atualizar(self, titulo: str, descricao: str, prioridade: int):
        if not titulo:
            raise ValueError("Título não pode ser vazio")
        
        if prioridade not in [p.value for p in PrioridadeEnum]:
            raise ValueError("Prioridade inválida")
        
        self._titulo = titulo
        self._descricao = descricao
        self._prioridade = prioridade