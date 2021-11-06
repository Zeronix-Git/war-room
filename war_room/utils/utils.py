from pathlib import Path

def mkdir_and_touch(path: str) -> None:
    path = Path(path)
    path.parent.mkdir(exist_ok = True, parents = True)
    path.touch(exist_ok = True)