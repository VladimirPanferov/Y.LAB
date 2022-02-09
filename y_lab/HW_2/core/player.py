import random

from typing import Final


def choose_first() -> str:
    return random.choice(PLAYER_MARKS)


PLAYER_MARKS: Final = ("X", "O")
CURRENT_PLAYER_MARK: str = choose_first()


def switch_player(mark: str) -> str:
    return "O" if mark == "X" else "X"
