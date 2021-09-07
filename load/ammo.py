import json
from typing import Callable

import click

from src.test_fixtures.tools import tasks_generator
from src.utils.config import load_config
CONFIG_PATH = "configs/config.yaml"


@click.command()
@click.option("--filename", prompt="ammo file", default="ammo.txt")
@click.option("--bullet_num", default=10000)
@click.option("--uri", prompt="uri to shoot")
def generate_post_requests(filename: str, uri: str, bullet_num: int) -> None:
    create_file(filename, uri, tasks_generator, bullet_num)


def create_file(filename: str, uri: str, payload_gen: Callable, bullet_num) -> None:
    config = load_config(CONFIG_PATH)
    with open(filename, "w") as f:
        f.write(f"[Host: {config['todo_app']['hostname']}]\n")
        f.write(f"[Content-type: application/json]\n")
        bullets = payload_gen(bullet_num)
        for bullet in bullets:
            json_bullet = json.dumps(bullet.__dict__)
            f.write(f"{len(json_bullet)} {uri}\n")
            f.write(f"{json_bullet}\n")


if __name__ == "__main__":
    generate_post_requests()



