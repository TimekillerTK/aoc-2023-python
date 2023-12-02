from pathlib import Path
from aoc_2023_python.lib.classes import Game
from aoc_2023_python.lib.consts import INPUTS


def input_loader(day: str) -> list[str]:
    file_path = Path(f"{INPUTS}/{day}.txt")
    try:
        with file_path.open("r") as file:
            lines = [line.rstrip("\n") for line in file]

    except FileNotFoundError:
        raise SystemExit(f"Error, could not find file in path {file_path}...")

    return lines


def cube_loader(day: str) -> list[Game]:
    file_path = Path(f"{INPUTS}/{day}.txt")
    try:
        with file_path.open("r") as file:
            lines = [Game.from_text_input(line) for line in file]

    except FileNotFoundError:
        raise SystemExit(f"Error, could not find file in path {file_path}...")

    return lines

