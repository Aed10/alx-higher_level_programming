#!/usr/bin/python3
"""101-nqueens.py"""


def isSafe(board, row, col):
    """Method that check if a queen can be placed on board[row][col].

    Args:
        board (list): list of list of integers.
        row (int): row of the board.
        col (int): column of the board.

    Returns:
        True if the queen can be placed, False otherwise.

    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    """Method that solve the N Queen problem using Backtracking.

    Args:
        board (list): list of list of integers.
        col (int): column of the board.

    Returns:
        True if the queen can be placed, False otherwise.

    """
    # base case: If all queens are placed
    # then return true
    if col >= len(board):
        return True
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(len(board)):
        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            # recur to place rest of the queens
            if solveNQUtil(board, col + 1) is True:
                return True
            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0
    # if the queen can not be placed in any row in
    # this colum col  then return false
    return False


def printSolution(board):
    """Method that print the solution.

    Args:
        board (list): list of list of integers.

    Returns:
        Always nothing.

    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end="")
        print()


def main():
    """Method that solve the N Queen problem.

    Args:
        Not arguments.

    Returns:
        Always nothing.

    """
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for j in range(n)] for i in range(n)]
    solveNQUtil(board, 0)
    printSolution(board)


if __name__ == "__main__":
    main()
