#!/usr/bin/python3
"""defines a class nchessboard"""
import sys


class NChessBoard:
    """NChessBoard class
    Attributes:
        n which is size
        board instance to layout the board
    """
    def __init__(self, n):
        """
        Instantiation of object
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def backtrack(self):
        """Method uses backtracking algorithm to place queens
        Returns:
            nothing
        """
        queen_positions = []
        self.backtrack_helper(0, queen_positions)
        if queen_positions:
            for s in queen_positions:
                self.print_board(s)
        else:
            print("solution does not exist")

    def backtrack_helper(self, column, queen_positions):
        """Method helps backtrack method
        Returns:
            all possible solultions of queen placement
        """
        if column == self.n:
            queens_pos = []
            for row in range(self.n):
                for column in range(self.n):
                    if self.board[row][column] == 1:
                        queens_pos.append([row, column])
            queen_positions.append(queens_pos)
            return True

        found_solution = False
        for row in range(self.n):
            if self.is_valid_sqr(row, column):
                self.board[row][column] = 1

                if self.backtrack_helper(column + 1, queen_positions):
                    found_solution = True

                self.board[row][column] = 0

        return found_solution

    def is_valid_sqr(self, row, column):
        """Method checks bounding conditions for queen placement
        Returns:
            a valid square for queen placement
        """
        for i in range(column):
            if self.board[row][i]:
                return False

        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if self.board[i][j]:
                return False

        for i, j in zip(range(row, self.n, 1), range(column, -1, -1)):
            if self.board[i][j]:
                return False

        return True

    def print_board(self, queen_positions):
        """prints the coordinates of q positions
        """
        for row in range(self.n):
            for column in range(self.n):
                if self.board[row][column] == 1:
                    queen_positions.append([row, column])
        print(queen_positions)


if __name__ == "__main__":
    """Main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    n_queens = NChessBoard(int(sys.argv[1]))
    queen_p = []
    n_queens.backtrack()
