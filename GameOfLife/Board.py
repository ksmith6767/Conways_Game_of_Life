from GameOfLife.Cell import Cell

import numpy as np


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        array = np.empty((width, height), Cell)

    def populateBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                self.array[i][j] = Cell(i, j, True)

    def printBoard(self):
        for i in range(self.width):
            print()
            for j in range(self.height):
                if self.array[i][j].getStatus():
                    print("O", end=" ")
                else:
                    print("X", end=" ")

    def checkNeighbors(self):





