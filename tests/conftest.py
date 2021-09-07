from typing import Dict

import pytest

from src.api.todo_api import TodoClient
from src.models.task import Task
from src.test_fixtures.tools import get_tasks_from_app, tasks_generator
from src.utils.config import load_config


@pytest.fixture(scope="session")
def config() -> Dict:
    return load_config("configs/config.yaml")


@pytest.fixture(scope="session")
def todo_client(config) -> TodoClient:
    return TodoClient(**config.get("todo_app"))


@pytest.fixture(scope="function")
def clear_tasks(todo_client, config) -> None:
    yield
    tasks = get_tasks_from_app(todo_client)
    for task in tasks:
        todo_client.delete_task(task.id, **config.get("auth"))


@pytest.fixture(scope="class")
def load_1000_tasks(todo_client: TodoClient, config) -> None:
    tasks = list(tasks_generator(1000))
    for t in tasks:
        todo_client.add_task(t)

    yield

    for t in tasks:
        todo_client.delete_task(t.id, **config.get("auth"))


@pytest.fixture(scope="class")
def add_task(todo_client: TodoClient, config) -> Task:
    task, *tail = tasks_generator(1)
    todo_client.add_task(task)

    yield task

    todo_client.delete_task(task.id, **config.get("auth"))
