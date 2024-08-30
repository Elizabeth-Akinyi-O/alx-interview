#!/usr/bin/python3
""" N Queens
n queens problem of placing n non-attacking queens on an n×n chessboard
solution requires that no two queens share the same row, column, or diagonal.
"""
import sys


def checkNqueensArgs(args):
    """ Check for validity of arguement of Nqueen. """
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(args[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except Exception:
        print("N must be a number")
        sys.exit(1)

    return N


def display_board(board):
    """ Print board of NxN."""
    for row in board:
        print(str(row).replace(',', '').replace('\'', ''))
    print()


def nQueens(board):
    """ n queens problem of placing n non-attacking queens on an n×n. """
    res = []
    for a in range(len(board)):
        temp = []
        for b in range(len(board)):
            if board[a][b] == 'Q':
                temp.append(a)
                temp.append(b)
        res.append(temp)
    print(res)


def isSafe(board, row, col):
    """Check if two queens threaten each other or not
    """
    # return False if two queen share the same column
    for a in range(row):
        if board[a][col] == 'Q':
            return False

    # return false if two queen share vertical diagonal
    (a, b) = (row, col)
    while a >= 0 and b >= 0:
        if board[a][b] == 'Q':
            return False
        a -= 1
        b -= 1

    # return false if two queen share the same '/' diagonal
    (a, b) = (row, col)
    while a >= 0 and b < len(board):
        if board[a][b] == 'Q':
            return False
        a -= 1
        b += 1

    return True


def chessBoard(board, row):
    """Create a ChessBoard of NxN
    """
    # if `N` queens are placed successfully, print the solution
    if row == len(board):
        nQueens(board)
        return

    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for a in range(len(board)):
        # if no two queens threaten each other
        if isSafe(board, row, a):
            # place queen on the current square
            board[row][a] = 'Q'

            # recur for the next row
            chessBoard(board, row + 1)

            #  backtrack and remove the queen from the current square\
            board[row][a] = '*'


if __name__ == "__main__":
    N = checkNqueensArgs(sys.argv)
    # Create board
    board = [["*" for a in range(N)] for b in range(N)]
    chessBoard(board, 0)
