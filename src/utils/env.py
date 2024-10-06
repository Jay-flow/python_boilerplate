import os
from os import getenv
from dotenv import load_dotenv
from root_path import PROJECT_ROOT_PATH


def get(name: str) -> str:
    load_dotenv(verbose=True, dotenv_path=os.path.join(PROJECT_ROOT_PATH, ".env"))
    value = getenv(name)

    if value is None:
        raise ValueError(f"No environmental variables were found. (key: {name}")

    return value
