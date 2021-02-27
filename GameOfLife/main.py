from GameOfLife.Cell import Cell

import numpy as np

# board arrays to store cells
board0 = np.empty((5, 6), Cell)
board1 = np.empty((5, 6), Cell)

# initializing the board
for i in range(5):
    for j in range(6):
        if i % 2 != 0:
            stat = True
        else:
            stat = False
        board0[i][j] = Cell(i, j, stat)

# printing the initialized board
for i in range(5):
    print()
    for j in range(6):
        if board0[i][j].getStatus():
            print("O", end=' ')
        else:
            print("X", end=' ')
print()
for i in range(5):
    for j in range(6):
        board1[i][j] = Cell(i, j, False)
        # counts the number of neighboring live cells
        lifeCount = 0

        # set/reset bounds for x-axis
        if i > 0:
            tempWidthStart = i - 1
        else:
            tempWidthStart = i
        if i < 4:
            tempWidthEnd = i + 1
        else:
            tempWidthEnd = i

        # nested loops that check the number of surrounding cells
        while tempWidthStart <= tempWidthEnd:

            # set/reset bounds for y-axis
            if j > 0:
                tempHeightStart = j - 1
            else:
                tempHeightStart = j
            if j < 5:
                tempHeightEnd = j + 1
            else:
                tempHeightEnd = j

            # height loop for surrounding cells
            while tempHeightStart <= tempHeightEnd:

                # keeps from including the current cell in lifeCount
                if tempWidthStart != i or tempHeightStart != j:

                    # if a neighbor cell is alive it is added to lifeCount
                    if board0[tempWidthStart][tempHeightStart].getStatus():
                        lifeCount += 1

                tempHeightStart += 1
            tempWidthStart += 1
        print(lifeCount)
        if board0[i][j].getStatus():
            if lifeCount == 3 or lifeCount == 2:
                board1[i][j].setStatus(True)
            else:
                board1[i][j].setStatus(False)
        elif board0[i][j].getStatus() == False:
            if lifeCount == 3:
                board1[i][j].setStatus(True)
            else:
                board1[i][j].setStatus(False)





for i in range(5):
    print()

    for j in range(6):

        if board1[i][j].getStatus():
            print("O", end=' ')

        else:
            print("X", end=' ')



