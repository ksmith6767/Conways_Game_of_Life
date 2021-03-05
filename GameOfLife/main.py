from GameOfLife.Cell import Cell

from GameOfLife.Board import Board

import numpy as np

import pygame as pygame

import random

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

switch = BLUE
for i in range(25):
    for j in range(25):
        pygame.draw.rect(screen, switch, (i*20, j*20, 18, 18))
        if switch == WHITE:
            switch = BLUE
        else:
            switch = WHITE

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# board arrays to store cells

board0 = np.empty((5, 6), Cell)
board1 = np.empty((5, 6), Cell)

# initializing the board
for i in range(5):
    for j in range(6):
        rand = random.randint(0, 1)
        if rand == 1:
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
for c in range(10):
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
            if board0[i][j].getStatus():
                if lifeCount == 3 or lifeCount == 2:
                    board1[i][j].setStatus(True)
                else:
                    board1[i][j].setStatus(False)
            elif not board0[i][j].getStatus():
                if lifeCount == 3:
                    board1[i][j].setStatus(True)
                else:
                    board1[i][j].setStatus(False)

    board0 = board1
    board1 = np.empty((5, 6), Cell)

    for i in range(5):
        print()

        for j in range(6):

            if board0[i][j].getStatus():
                print("O", end=' ')

            else:
                print("X", end=' ')
    print()

print("*************")
print()

new_board = Board(5, 6)
new_board1 = Board(5, 6)

new_board.clear()

new_board1.populateBoard()

new_board.populateBoard()


new_board.printBoard()

for i in range(5):
    for j in range(6):

        new_board1.getCell(i, j).setStatus(new_board.checkNeighbors(i, j))

new_board = new_board1
print()

new_board.printBoard()




