from GameOfLife.Cell import Cell

import numpy as np

# board arrays to store cells
board0 = np.empty((5, 5), Cell)
board1 = np.empty((5, 5), Cell)

i = 0
j = 0

# initializing the board
for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            stat = True
        else:
            stat = False
        board0[i][j] = Cell(i, j, stat)

# printing the initialized board
for i in range(5):
    print()
    for j in range(5):
        if board0[i][j].getStatus():
            print("O", end=' ')
        else:
            print("X", end=' ')
