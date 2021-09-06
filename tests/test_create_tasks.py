import pytest

from src.api.todo_api import TodoClient
from src.models.task import Task
from src.test_fixtures.tools import tasks_generator, get_tasks_from_app


@pytest.mark.parametrize("task", tasks_generator(5))
def test_create_task(task, todo_client: TodoClient, clear_tasks):
    resp = todo_client.add_task(task)
    assert resp.status_code == 201

    task_db, *tail = [i for i in get_tasks_from_app(todo_client) if i.id == task.id]
    assert task_db == task


@pytest.mark.parametrize("task", tasks_generator(1))
def test_create_tasks_with_same_id(task, todo_client: TodoClient, clear_tasks):
    create_fst = todo_client.add_task(task)
    assert create_fst.status_code == 201

    create_snd = todo_client.add_task(task)
    assert create_snd.status_code == 400


@pytest.mark.parametrize("task_1, task_2", [(Task(0, "x", False), Task(1, "x", True))])
def test_create_tasks_with_same_desc(task_1, task_2, todo_client: TodoClient, clear_tasks):
    todo_client.add_task(task_1)
    todo_client.add_task(task_2)

    t_1, t_2 = tasks = get_tasks_from_app(todo_client)
    assert len(tasks) == 2
    assert t_1.text == t_2.text


@pytest.mark.parametrize("task", [Task(0, "", True)])
def test_create_task_empty_text(task, todo_client: TodoClient, clear_tasks):
    r = todo_client.add_task(task)
    assert r.status_code == 201

    t, *tail = get_tasks_from_app(todo_client)
    assert t.text == ""


def test_create_task_improper_values():
    pass
