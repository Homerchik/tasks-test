from typing import Iterator, List
from uuid import uuid4

from src.api.todo_api import TodoClient
from src.models.task import Task
from src.utils.base_utils import rand_bool


def tasks_generator(n: int) -> Iterator[Task]:
    """generates generator consisting of n random tasks"""
    return (Task(i, str(uuid4()), rand_bool()) for i in range(n))


def get_tasks_from_app(todo_client: TodoClient, limit: int = None, offset: int = None) -> List[Task]:
    r = todo_client.tasks(offset, limit)
    return [Task(**i) for i in r.json()]