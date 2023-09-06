#!/usr/bin/python3
import sys


class Queen:
    """Create an object called Queen.
    Attributes:
        N: The size of our board(N*N), and the number of queens.
        positions: List of all possible positions for the queen obj.
    """
    def __init__(self, N):
        """Initialize our object.
        Args:
            N: The size of our board(N*N), and the number of queens.

        """
        self.N = N
        self.solutions = []
        self.solve(0, [])

    def is_safe(self, row, col, positions):
        """Check if a given position is safe.

        Args:
            row: a given row.
            col: a given column.
            positions: The previous occupied positions.
        """
        for prev_row, prev_col in positions:
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    def solve(self, row, positions):
        """Give all possible solutions.

        Args:
            row: A giev row.
            positions: list stores the positions of queens placed in the board.
        """
        if row == self.N:
            self.solutions.append(positions[:])
            return
        for col in range(self.N):
            if self.is_safe(row, col, positions):
                positions.append([row, col])
                self.solve(row + 1, positions)
                positions.pop()


def main():
    if len(sys.argv) != 2:
        print('Usage: python nqueens.py N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    queen = Queen(N)
    """
    To print Graphically the solution.
    for solution in queen.solutions:
        for row, col in solution:
           # print('.' * col + 'Q' + '.' * (N - col - 1))
            print([row, col], end = ", ")
        print()
        """
    for i in range(len(queen.solutions)):
        print(queen.solutions[i])


if __name__ == "__main__":
    main()
