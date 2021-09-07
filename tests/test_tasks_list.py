import random
import pytest

from src.api.todo_api import TodoClient
from src.models.task import Task
from src.test_fixtures.tools import get_tasks_from_app


def test_empty_task_list(todo_client: TodoClient):
    tasks = get_tasks_from_app(todo_client)
    assert not tasks


@pytest.mark.skip
@pytest.mark.parametrize("t_1, t_2", [(Task(2, "x", True), Task(1, "x", True))])
def test_tasks_ordered_by_id(t_1: Task, t_2: Task, todo_client: TodoClient, clear_tasks):
    todo_client.add_task(t_1)
    todo_client.add_task(t_2)

    tasks = get_tasks_from_app(todo_client)
    assert tasks[0].id < tasks[1].id


@pytest.mark.usefixtures("load_1000_tasks", "todo_client", "config")
class TestOnTasksBundle:
    total_tasks: int = 1000

    @pytest.mark.parametrize("limit", [random.randint(1, 500) for i in range(5)])
    def test_task_list_limit(self, limit, todo_client):
        tasks = get_tasks_from_app(todo_client, limit=limit)
        assert len(tasks) == limit

    @pytest.mark.parametrize("offset", [random.randint(1, 999) for j in range(5)])
    def test_task_list_offset(self, offset, todo_client):
        tasks = get_tasks_from_app(todo_client, offset=offset)
        assert len(tasks) == self.total_tasks - offset

    @pytest.mark.parametrize("limit,offset", [(random.randint(0, 500), random.randint(1, 500))])
    def test_tasks_limit_and_offset(self, limit, offset, todo_client):
        all_tasks = get_tasks_from_app(todo_client)
        tasks_with_filters = get_tasks_from_app(todo_client, limit=limit, offset=offset)

        assert all_tasks[offset: offset+limit] == tasks_with_filters
