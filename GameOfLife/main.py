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


for i in range(5):
    print("i loop")
    for j in range(5):
        print("j loop")
        lifeCount = 0
        # helper variables to get the bound of area around cell
        # if/else keep from trying to access elements that are outside of bounds

        # bounds for x-axis
        if board0[i][j].getx() > 0:
            tempWidthStart = board0[i][j].getx() - 1
        else:
            tempWidthStart = board0[i][j].getx()
        if board0[i][j].getx() < 4:
            tempWidthEnd = board0[i][j].getx() + 1
        else:
            tempWidthEnd = board0[i][j].getx()

        # bounds for y-axis
        if board0[i][j].gety() > 0:
            tempHeightStart = board0[i][j].gety() - 1
        else:
            tempHeightStart = board0[i][j].gety()
        if board0[i][j].gety() < 4:
            tempHeightEnd = board0[i][j].gety() + 1
        else:
            tempHeightEnd = board0[i][j].gety()

        # nested loops that check the number of surrounding cells
        while tempWidthStart <= tempWidthEnd:
            print("width loop")

            # height loop for surrounding cells
            while tempHeightStart <= tempHeightEnd:
                print("height loop")

                # keeps from including the current cell in lifeCount
                if board0[i][j].getx() != i & board0[i][j].gety() != j:

                    # if a neighbor cell is alive it is added to lifeCount
                    if board0[tempWidthStart][tempHeightStart].getStatus():
                        lifeCount = lifeCount + 1
                        print(lifeCount)
                tempHeightStart += 1

                
                if lifeCount == 3 | lifeCount == 2:
                    board1[i][j] = Cell(i, j, True)

                else:
                    board1[i][j] = Cell(i, j, False)
            tempWidthStart += 1

for i in range(5):
    print()

    for j in range(5):

        if board1[i][j].getStatus():
            print("O", end=' ')

        else:
            print("X", end=' ')



