from typing import Optional, Dict, Any

import requests
from requests import Response
from requests.auth import HTTPBasicAuth

from src.models.task import Task


class TodoClient:
    def __init__(self, hostname: str, port: str):
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json", "Content-type": "application/json"})
        self.hostname = hostname
        self.port = port

    @staticmethod
    def __add_query_string(args: Dict) -> Dict[str, Any]:
        qs = {}
        for k, v in args.items():
            if v:
                qs[k] = v
        return qs

    def __make_req(self, method: str, api: str, params: Optional[Dict] = None,
                   payload: Optional[Dict] = None) -> Response:
        return self.session.request(url=f"http://{self.hostname}:{self.port}/{api}", method=method,
                                    data=params, json=payload)

    def tasks(self, offset: int = None, limit: int = None) -> Response:
        return self.__make_req("get", "todos", params=self.__add_query_string({"offset": offset, "limit": limit}))

    def add_task(self, t: Task) -> Response:
        return self.__make_req("post", "todos", payload=t.__dict__)

    def update_task(self, id_: int, t: Task) -> Response:
        return self.__make_req("put", f"todos/{id_}", payload=t.__dict__)

    def delete_task(self, id_: int, user: str, pwd: str) -> Response:
        self.session.auth = HTTPBasicAuth(user, pwd)
        r = self.__make_req("delete", f"todos/{id_}")
        self.session.auth = None
        return r

