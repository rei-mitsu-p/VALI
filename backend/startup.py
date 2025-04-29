from os import name
from pathlib import Path
from subprocess import run


def start_uvicorn() -> None:
    run(
        [
            str(Path(".venv") / ("Scripts" if name == "nt" else "bin") / "python"),
            "-m",
            "uvicorn",
            "app.main:app",
            "--reload",
            "--http",
            "httptools",
        ]
    )


if __name__ == "__main__":
    start_uvicorn()
