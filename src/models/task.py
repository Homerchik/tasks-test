from dataclasses import dataclass


@dataclass
class Task:
    id: int
    text: str
    completed: bool