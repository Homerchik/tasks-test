from typing import Dict

import pytest

from src.api.todo_api import TodoClient
from src.test_fixtures.tools import get_tasks_from_app
from src.utils.config import load_config


@pytest.fixture(scope="session")
def config() -> Dict:
    return load_config("../configs/config.yaml")


@pytest.fixture(scope="session")
def todo_client(config) -> TodoClient:
    return TodoClient(**config.get("todo_app"))


@pytest.fixture(scope="function")
def clear_tasks(todo_client, config) -> None:
    yield
    tasks = get_tasks_from_app(todo_client)
    for task in tasks:
        todo_client.delete_task(task.id, **config.get("auth"))