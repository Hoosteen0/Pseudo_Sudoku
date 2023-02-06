# imports
import numpy as np


class Generator:
    def __init__(self, n, m):
        self._board = self.new_board(n, m)

    def new_board(self, n, m):
        # make a 2d array with all values set to 0
        board = np.zeros(shape=(n, n), dtype=np.uint8)
        print(board.view())

        # initialize the set of numbers from 1 to n.
        numbers = set()
        for i in range(1, n + 1):
            numbers.add(i)
        print(numbers)

        # copy numbers for each row, and assign values
        for row in range(0, board.shape[0]):
            # copy the set
            row_numbers = numbers.copy()

            for col in range(0, board.shape[1]):

                # need to randomly pull from the set here, will call to a helper function
                data = row_numbers.pop()

                # assign pulled number to its new spot
                board[row, col] = data

                # will need to check for 'collisions'

        print(board.view())
        return board
