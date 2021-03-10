
from GameOfLife.Board import Board

import pygame

# define the screen as 500X500 pixels
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))

# color definitions
WHITE = (50, 50, 50)
BLUE = (0, 50, 205)

# define the bounds of the board
WIDTH = 25
HEIGHT = 25

# switcher variable for cell colors
switch = BLUE

clock = pygame.time.Clock()

# create new board and temp board for updating purposes
board = Board(WIDTH, HEIGHT)
board1 = Board(WIDTH, HEIGHT)

board.populateBoard()
board1.clear()

# MAIN GAME LOOP
run = True
while run:

    #    block to draw the representation of the board
    for i in range(WIDTH):
        for j in range(HEIGHT):

            if board.getCell(i, j).getStatus():
                switch = BLUE
            else:
                switch = WHITE

            pygame.draw.rect(screen, switch, (i * 20, j * 20, 18, 18))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("press")
                for i in range(WIDTH):
                    for j in range(HEIGHT):
                        board1.getCell(i, j).setStatus(board.checkNeighbors(i, j))
                for i in range(WIDTH):
                    for j in range(HEIGHT):
                        board.getCell(i, j).setStatus(board1.getCell(i, j).getStatus())

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            x = int(x/20)
            y = int(y/20)
            print(x, y)
            if not board.getCell(x, y).getStatus():
                board.getCell(x, y).setStatus(True)
            else:
                board.getCell(x, y).setStatus(False)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("press r")
                board.populateBoard()

    pygame.time.delay(100)
