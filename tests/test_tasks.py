import pytest
from app.application.services.tasks_services import TaskService

#RODAR O ARQUIVO DE TESTE
#python -m pytest -v

#RODAR UM TEST ESPECÍFICO. EXEMPLO:
#python -m pytest -k test_criar_task

@pytest.fixture
def service():
    return TaskService()


def test_criar_task(service):
    task = service.criar('teste 1', 'descrição teste', 1)

    lista = service.listar()
    assert len(lista) == 1
    assert lista[0].titulo == 'teste 1'
    assert lista[0].descricao == 'descrição teste'
    assert lista[0].prioridade == 1
    assert lista[0].concluida is False


def test_listar_tasks(service):
    service.criar('t1', 'd1', 1)
    service.criar('t2', 'd2', 1)

    lista = service.listar()

    assert len(lista) == 2


def test_obter_task(service):
    task = service.criar('t1', 'd1', 1)

    task_obtida = service.obter(task.id)

    assert task_obtida.id == task.id
    assert task_obtida.titulo == 't1'


def test_obter_task_inexistente(service):
    from uuid import uuid4

    with pytest.raises(Exception, match="Task não encontrada"):
        service.obter(uuid4())


def test_atualizar_task(service):
    task = service.criar('t1', 'd1', 1)

    task_atualizada = service.atualizar(task.id, 'novo titulo', 'nova descricao', 3)

    assert task_atualizada.titulo == 'novo titulo'
    assert task_atualizada.descricao == 'nova descricao'
    assert task_atualizada.prioridade == 3


def test_concluir_task(service):
    task = service.criar('t1', 'd1', 1)

    task_concluida = service.concluir(task.id)

    assert task_concluida.concluida is True


def test_concluir_task_ja_concluida(service):
    task = service.criar('t1', 'd1', 1)
    service.concluir(task.id)

    with pytest.raises(Exception, match="Tarefa já está concluída"):
        service.concluir(task.id)


def test_remover_task(service):
    task = service.criar('t1', 'd1', 1)

    service.remover(task.id)

    lista = service.listar()
    assert len(lista) == 0


def test_remover_task_inexistente(service):
    from uuid import uuid4

    with pytest.raises(Exception, match="Task não encontrada"):
        service.remover(uuid4())