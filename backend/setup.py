from os import name
from subprocess import run
from sys import executable
from pathlib import Path


def create_virtual_environment():
    virtual_environment_directory: Path = Path(".venv")
    if not virtual_environment_directory.exists():
        run([executable, "-m", "venv", str(virtual_environment_directory)])
        python_executable: Path = (
            virtual_environment_directory
            / ("Scripts" if name == "nt" else "bin")
            / "python"
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
    create_virtual_environment()
