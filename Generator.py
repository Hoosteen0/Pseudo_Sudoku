# imports
import random
import numpy as np


def rand_choice(available_choices):
    index = random.randint(0, len(available_choices)-1)
    choice = available_choices[index]
    del available_choices[index]
    return choice


class Generator:
    def __init__(self, n, m):
        # self._board = self.new_board(n, m)
        self._other_board = self.alt_board(n, m)

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
            index = random.randint(0, len(row_num) - 1)
            data = row_num[index]
            del row_num[index]
            del col_num[index]
            board[intersect, intersect] = data

            # still need to check left if col-wise or above if row-wise for collisions
            # run loop to assign rest in col
            for k in range(intersect+1, board.shape[0]):
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
                board[k, intersect] = data
                col_num.extend(temp_list)
            # run loop to assign rest in row
            for l in range(intersect+1, board.shape[0]):
                data = rand_choice(row_num)

                temp_list_vert = []
                for p in range(intersect-1, -1, -1):
                    if data == board[p, l]:
                        temp_list_vert.append(data)
                        data = rand_choice(row_num)
                board[intersect, l] = data
                row_num.extend(temp_list_vert)
        print(board.view())
        return board

    def new_board(self, n, m):
        # make a 2d array with all values set to 0
        board = np.zeros(shape=(n, n), dtype=np.uint8)
        print(board.view())

        # initialize the set of numbers from 1 to n.
        numbers = list()
        for i in range(1, n + 1):
            numbers.append(i)
        print(numbers)

        # copy numbers for each row, and assign values
        for row in range(0, board.shape[0]):
            # copy the set
            row_numbers = numbers.copy()

            for col in range(0, board.shape[1]):

                # need to randomly pull from the set here, will call to a helper function
                # data = row_numbers.pop()
                data = rand_choice(row_numbers)

                # assign pulled number to its new spot
                board[row, col] = data

                # will need to check for 'collisions'

        print(board.view())
        return board
