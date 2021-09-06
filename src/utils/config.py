from typing import Dict

import yaml


def load_config(filename: str) -> Dict:
    with open(filename, "r") as f:
        return yaml.safe_load(f.read())
