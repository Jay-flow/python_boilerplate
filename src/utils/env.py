from os import getenv

from dotenv import load_dotenv


def get(name: str) -> str:
    load_dotenv(verbose=True)
    value = getenv(name)

    if value is None:
        raise ValueError(
            f'No environmental variables were found. (key: {name}')

    return value
