#!/usr/bin/python3
"""
N Queens problem solver
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
"""
import sys


def check_nqueens_args(args):
    """Check the validity of arguments for the N-Queens problem"""
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(args[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    return N


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check the same column in previous rows
    for i in range(row):
        if board[i] == col:
            return False

    # Check the main diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check the anti-diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N, row, board, solutions):
    """Recursively solve the N-Queens problem"""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            # Backtrack happens automatically as the recursion unwinds


def print_solutions(solutions):
    """Print all the valid solutions"""
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Validate the command-line arguments and get the board size N
    N = check_nqueens_args(sys.argv)

    # Prepare to collect all solutions
    # Initialize the board where board[i] is the column of the queen in row i
    board = [-1] * N
    solutions = []

    # Solve the N-Queens problem
    solve_nqueens(N, 0, board, solutions)

    # Print all solutions
    print_solutions(solutions)
