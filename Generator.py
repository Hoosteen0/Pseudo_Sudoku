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

    def alt_board(self, n, m):
        # make a 2d array with all values set to 0
        board = np.zeros(shape=(n, n), dtype=np.uint8)
        print(board.view())

        # initialize the set of numbers from 1 to n.
        numbers = list()
        for i in range(1, n + 1):
            numbers.append(i)
        print(numbers)

        # intersect is where the row and col are =
        for intersect in range(0, board.shape[0]):
            row_num = numbers.copy()
            col_num = numbers.copy()
            # check back to previous rows to eliminate collisions
            for i in range(intersect-1, -1, -1):
                col_num.remove(board[i, intersect])
            # check back previous cols to eliminate collisions
            # error that happened here, tried to remove a value that was no longer in the list, because there
            #  were two instances of the same number in the row (i.e. 1, 5, 5, 0) looks left then removes 5; then
            #   5 is no longer present to remove from list; throws an error; soln is to check left for rows, and
            #    above for cols for collisions before placing
            for j in range(intersect-1, -1, -1):
                row_num.remove(board[intersect, j])
            # now we've removed collisions from previous iterations

            # randomly pick a number from row_num for the corner shared between the row and col
            index = rand.randint(0, len(row_num) - 1)
            data = row_num[index]
            del row_num[index]
            del col_num[index]
            board[intersect, intersect] = data

            # still need to check left if col-wise or above if row-wise for collisions
            # run loop to assign rest in col
            k = intersect + 1
            while k < board.shape[0]:
            # for k in range(intersect+1, board.shape[0]):
                data = rand_choice(col_num)
                # check left to see if values match data
                temp_list = []
                for o in range(intersect-1, -1, -1):
                    # new error, only remaining value in the list is already assigned in the row/list, which means
                    #  we have to backtrack TO-DO
                    if data == board[k, o]:
                        # hold data in a temp list, and try again until you find something that works
                        temp_list.append(data)
                        data = rand_choice(col_num)
                        if data is None:
                            # backtrack here by undoing everything up to the intersection,
                            for p in range(k, intersect+1, -1):
                                col_num.append(board[p, intersect])
                                board[p, intersect] = 0
                            k = intersect + 1
                            #  keeping the intersection value in a temp variable, and picking from what's left?
                board[k, intersect] = data
                col_num.extend(temp_list)
                k = k + 1
            # run loop to assign rest in row
            l = intersect + 1
            while l < board.shape[0]:
            # for l in range(intersect+1, board.shape[0]):
                data = rand_choice(row_num)

                temp_list_vert = []
                for p in range(intersect-1, -1, -1):
                    if data == board[p, l]:
                        temp_list_vert.append(data)
                        data = rand_choice(row_num)
                        if data is None:
                            for q in range(l, intersect+1, -1):
                                row_num.append(board[intersect, q])
                                board[intersect, q] = 0
                            l = intersect + 1
                board[intersect, l] = data
                row_num.extend(temp_list_vert)
                l = l + 1
        print(board.view())
        return board

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
        print(self._board)
        for m in range(1, self._m + 1):

            rand_row = rand.randint(0, self._n - 1)
            rand_col = rand.randint(0, self._n - 1)
            while self._board[rand_row][rand_col] == 0:
                rand_row = rand.randint(0, self._n - 1)
                rand_col = rand.randint(0, self._n - 1)

            # found a valid rand coord
            self._board[rand_row][rand_col] = 0
        print(self._board)
