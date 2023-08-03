#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given row and column in the board.

    Args:
        board (list): The current state of the board with the position of queens.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.

    Returns:
        bool: True if it is safe to place the queen at the given position, False otherwise.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursively solve the N queens problem using backtracking.

    Args:
        board (list): The current state of the board with the position of queens.
        row (int): The current row being processed.
        n (int): The size of the chessboard (N).

    Prints:
        All the possible solutions to the N queens problem in the required format.
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """
    Main function to solve the N queens problem.

    Args:
        n (int): The size of the chessboard (N).

    Prints:
        If N is not valid, it prints an error message and exits the program with status 1.
        If N is valid, it prints all the possible solutions to the N queens problem.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
