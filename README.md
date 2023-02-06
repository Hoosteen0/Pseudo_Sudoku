# Pseudo_Sudoku
Create a program that generates a solvable pseudo-sudoku board, and have an algorithm solve the board. Plot the size of the board, with m number of removed tiles against the time it takes to solve


## Strategy
1. In the main file, we will be returning a data point every run of the dfs, where n will be plotted against time, with each graph being a different m.
2. We will use numpy to initialize an array to represent the graph.
3. Everything will be initialized to 0
4. 