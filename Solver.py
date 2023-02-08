# imports
import timeit

import numpy as np


class Solver:
    def __init__(self, board, n, m):
        self._m = m
        self._n = n
        self._board = board
        self._stack = []
        self._zero_indices = []
        self._board_size = range(1, n + 1)
        duration = self.time()
        print(f'Time taken = {duration}')

    def time(self):
        start = timeit.default_timer()
        self.solve(self._board)
        end = timeit.default_timer()
        return end - start

    def solve(self, board):
        # get an array of indices for the 0s
        self._zero_indices = np.argwhere(board == 0)
        self.dfs(0, self._stack)

    def test_state(self, current_stack):
        check_arr = np.arange(1, self._n+1)
        curr_board = self._board.copy()
        for k in range(len(self._zero_indices)):
            curr_board[self._zero_indices[k][0]][self._zero_indices[k][1]] = current_stack[k]
        for i in range(self._n):
            if not np.array_equal(np.unique(curr_board[i]), check_arr):
                return False
        for j in range(self._n):
            if not np.array_equal(np.unique(curr_board[:, j]), check_arr):
                return False
        print(f'\nSolved board is\n{curr_board}')
        return True
    def dfs(self, current_depth, current_stack):
        if self._m == current_depth:
            if self.test_state(current_stack):
                self._stack = current_stack
                return True
            else:
                return False
        for number in self._board_size:
            current_stack.append(number)
            if self.dfs(current_depth + 1, current_stack):
                return True
            current_stack.pop()
        return False
