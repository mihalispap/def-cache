from pathlib import Path


def directory_exists(dirpath: str) -> bool:
    return Path(dirpath).exists()


def create_directory(dirpath: str) -> None:
    Path(dirpath).mkdir(parents=True, exist_ok=True)
