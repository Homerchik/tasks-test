from typing import Dict

import pytest

from src.api.todo_api import TodoClient
from src.models.task import Task
from src.test_fixtures.tools import get_tasks_from_app


@pytest.mark.parametrize("task", [Task(1, "xyz", True)])
def test_task_delete(task, todo_client: TodoClient, config: Dict):
    todo_client.add_task(task)

    tasks = get_tasks_from_app(todo_client)
    assert tasks

    r = todo_client.delete_task(task.id, **config.get("auth"))
    assert r.status_code == 204

    tasks_after_del = get_tasks_from_app(todo_client)
    assert len(tasks_after_del) == len(tasks) - 1


@pytest.mark.parametrize("task", [Task(1000, "xyz", True)])
def test_task_delete_wrong_cred(task, todo_client: TodoClient, clear_tasks):
    todo_client.add_task(task)

    tasks = get_tasks_from_app(todo_client)
    assert tasks

    r = todo_client.delete_task(task.id, "1", "1")
    assert r.status_code == 401

    task_after, *tail = tasks_after_del = get_tasks_from_app(todo_client)
    assert len(tasks_after_del) == len(tasks)
    assert task_after == task
