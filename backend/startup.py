from os import name
from subprocess import run
from pathlib import Path


def start_uvicorn():
    run(
        [
            str(Path(".venv") / ("Scripts" if name == "nt" else "bin") / "python"),
            "-m",
            "uvicorn",
            "app.main:app",
            "--reload",
        ]
    )


if __name__ == "__main__":
    start_uvicorn()
