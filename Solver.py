# imports
import numpy as np


class Solver:
    def __init__(self, board, n):
        self._n = n
        self._board = board
        self._stack = []
        self._tree = []
        self.solve(self._board)

    def solve(self, board):
        # get an array of indices for the 0s
        self._tree = np.argwhere(board == 0)
        self.dfs(self._tree)

    def dfs(self, zeros_coords):
        pass

