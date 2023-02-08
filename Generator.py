# imports
import random as rand
import numpy as np


def rand_choice(available_choices):
    if len(available_choices) is None:
        return None
    index = rand.randint(0, len(available_choices)-1)
    choice = available_choices[index]
    del available_choices[index]
    return choice


class Generator:
    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._board = self.new_board()
        self.remove_m()

    def get_board(self):
        return self._board


    def new_board(self):
        n = self._n
        num_list = list(range(1, n + 1))

        board = np.zeros((n, n), dtype=int)
        while np.any(np.isin(board, 0)):
            board = np.zeros((n, n), dtype=int)
            for val in num_list:
                valid_col = list(range(n))
                for i in range(board[0].size):
                    rand_col = rand.choice(valid_col)
                    loop_count = 0
                    while board[i][rand_col] != 0 or rand_col not in valid_col:
                        rand_col = (rand_col + 1) % n
                        loop_count += 1
                        if loop_count >= n:
                            break
                    board[i][rand_col] = val
                    valid_col.remove(rand_col)

        # print()
        # print("Finished")
        # print(board)
        return board

    def remove_m(self):
        print(f'Initially solved board is\n{self._board}')
        for m in range(1, self._m + 1):

            rand_row = rand.randint(0, self._n - 1)
            rand_col = rand.randint(0, self._n - 1)
            while self._board[rand_row][rand_col] == 0:
                rand_row = rand.randint(0, self._n - 1)
                rand_col = rand.randint(0, self._n - 1)

            # found a valid rand coord
            self._board[rand_row][rand_col] = 0
        print(f'\nRemoved board is\n{self._board}')
