#!/usr/bin/python3

""" N Queens
n queens problem of placing n non-attacking queens on an n×n chessboard.
Solution requires that no two queens share the same row, column, or diagonal.
"""
import sys


def checkNqueensArgs(args):
    """ Check for validity of argument of Nqueen. """
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


def nQueens(board):
    """ Prints the board configuration showing the positions of the queens. """
    res = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'Q':
                res.append([i, j])
    print(res)


def isSafe(board, row, col):
    """ Check if two queens threaten each other or not. """
    # Check the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the upper-left diagonal
    (i, j) = (row, col)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    (i, j) = (row, col)
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def chessBoard(board, row):
    """ Create a ChessBoard of NxN """
    # If N queens are placed successfully, print the solution
    if row == len(board):
        nQueens(board)
        return

    # Try placing a queen in each column of the current row
    for i in range(len(board)):
        if isSafe(board, row, i):
            # Place queen on the current square
            board[row][i] = 'Q'

            # Recur for the next row
            chessBoard(board, row + 1)

            # Backtrack and remove the queen from the current square
            board[row][i] = '*'


if __name__ == "__main__":
    N = checkNqueensArgs(sys.argv)
    # Create board
    board = [["*" for i in range(N)] for j in range(N)]
    chessBoard(board, 0)
