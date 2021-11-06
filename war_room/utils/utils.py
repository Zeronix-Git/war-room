from pathlib import Path


def mkdir_and_touch(path: str) -> None:
    _path = Path(path)
    _path.parent.mkdir(exist_ok=True, parents=True)
    _path.touch(exist_ok=True)
