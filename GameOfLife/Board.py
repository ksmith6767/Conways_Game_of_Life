from GameOfLife.Cell import Cell

import numpy as np

import random


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = np.empty((width, height), Cell)

    def populateBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                stat = False
                rand = random.randint(0, 8)

                if rand == 1:
                    stat = True
                else:
                    stat = False

                self.array[i][j] = Cell(i, j, stat)

    def printBoard(self):
        for i in range(self.width):
            print()
            for j in range(self.height):
                if self.array[i][j].getStatus():
                    print("O", end=" ")
                else:
                    print("X", end=" ")

    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                self.array[i][j] = Cell(i, j, False)

    def getCell(self, x, y):
        return self.array[x][y]

    def checkNeighbors(self, i, j):

        lifeCount = 0

        # set/reset bounds for x-axis
        if i > 0:
            tempWidthStart = i - 1
        else:
            tempWidthStart = i
        if i < self.width-1:
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
            if j < self.height-1:
                tempHeightEnd = j + 1
            else:
                tempHeightEnd = j

            # height loop for surrounding cells

            while tempHeightStart <= tempHeightEnd:

                # keeps from including the current cell in lifeCount
                if tempWidthStart != i or tempHeightStart != j:

                    # if a neighbor cell is alive it is added to lifeCount
                    if self.array[tempWidthStart][tempHeightStart].getStatus():
                        lifeCount += 1

                tempHeightStart += 1
            tempWidthStart += 1

        if self.array[i][j].getStatus():
            if lifeCount == 3 or lifeCount == 2:
                return True
            else:
                return False
        else:
            if lifeCount == 3:
                return True
            else:
                return False

