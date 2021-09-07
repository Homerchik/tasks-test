import pytest

from src.api.todo_api import TodoClient
from src.test_fixtures.tools import get_tasks_from_app


@pytest.mark.usefixtures("add_task")
class TestTaskUpdate:
    def test_text_can_be_updated(self, todo_client: TodoClient, add_task):
        task = add_task
        cur_task, *tail = get_tasks_from_app(todo_client)
        assert cur_task == task

        task.text = "new text"
        r = todo_client.update_task(task.id, task)
        assert r.status_code == 200
        cur_task, *tail = get_tasks_from_app(todo_client)
        assert task == cur_task

    def test_completed_flag_can_be_updated(self, add_task, todo_client):
        task = add_task
        cur_task, *tail = get_tasks_from_app(todo_client)
        assert cur_task == task

        task.completed = not task.completed
        r = todo_client.update_task(task.id, task)
        assert r.status_code == 200
        cur_task, *tail = get_tasks_from_app(todo_client)
        assert task == cur_task

    @pytest.mark.skip
    def test_id_cant_be_updated(self, todo_client, add_task):
        task = add_task
        id_ = task.id
        task.id = 800
        r = todo_client.update_task(id_, task)
        assert r.status_code == 400
