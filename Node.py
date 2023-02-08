# imports

class Node:
    def __init__(self, value, n):
        self._data = value
        self._children = [range(1, n + 1)]

    def update_value(self, new_value):
        self._data = new_value
