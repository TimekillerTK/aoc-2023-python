from pathlib import Path

from aoc_2023_python.lib.consts import INPUTS


def input_loader(day: str) -> list[str]:
    file_path = Path(f"{INPUTS}/{day}.txt")
    try:
        with file_path.open("r") as file:
            lines = [line.rstrip("\n") for line in file]

    except FileNotFoundError:
        raise SystemExit(f"Error, could not find file in path {file_path}...")

    return lines
