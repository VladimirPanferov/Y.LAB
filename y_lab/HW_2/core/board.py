import os

from typing import (
    Final,
    NoReturn,
    Tuple,
)

import numpy as np

import player


NUM_COLS: Final = 10
NUM_ROWS: Final = 10

PLAY_BOARD = np.full((NUM_COLS, NUM_ROWS), " ")


def clear_screen() -> NoReturn:
    os_name = os.name
    if os_name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def display_board(board: np.ndarray) -> NoReturn:
    clear_screen()
    print("    ", end="")
    print(" | ".join(map(str, range(board.shape[0]))), end=" |\n")

    for row in range(board.shape[0]):
        print("   ", end="")
        print("----"* board.shape[0])
        print(row, end=" | ")
        print(" | ".join(board[row]), end=" |\n")


def space_check(board: np.ndarray, position: Tuple[int, int]) -> bool:
    return board[position] not in player.PLAYER_MARKS


def full_board_check(board: np.ndarray) -> bool:
    return len(board[np.where(board == " ")]) == 0


print(full_board_check(PLAY_BOARD))
