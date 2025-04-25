from os import name
from pathlib import Path
from subprocess import run
from sys import executable


def create_virtual_env() -> None:
    virtual_env_dir = Path(".venv")
    if not virtual_env_dir.exists():
        run([executable, "-m", "venv", str(virtual_env_dir)])
        python_executable = (
            virtual_env_dir / ("Scripts" if name == "nt" else "bin") / "python"
        )
        run(
            [
                str(python_executable),
                "-m",
                "pip",
                "install",
                "-r",
                "requirements.txt",
            ]
        )


if __name__ == "__main__":
    create_virtual_env()
