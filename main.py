# imports
import Generator
import Solver


def main():
    # make a new board with generator

    # pass board to Solver
    n = int(input("Enter size of nxn puzzle"))
    m = int(input("Enter number of removed tiles"))
    # output board?
    new_generator = Generator.Generator(n, m)
    new_board = new_generator.get_board()
    new_solver = Solver.Solver(new_board, n, m)


main()
