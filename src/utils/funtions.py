from pathlib import Path


def create_the_directory(output_path: str) -> None:
    Path(output_path).mkdir(parents=True, exist_ok=True)
