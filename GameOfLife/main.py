
from GameOfLife.Board import Board

import pygame

# define the screen as 500X500 pixels
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))

# color definitions
WHITE = (50, 50, 50)
BLUE = (0, 200, 55)

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
board1.populateBoard()

# MAIN GAME LOOP
run = True
while run:


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
                if switch == BLUE:
                    switch = WHITE
                else:
                    switch = BLUE

    for i in range(WIDTH):
        for j in range(HEIGHT):
            board1.getCell(i, j).setStatus(board.checkNeighbors(i,j))

    board = board1


    pygame.time.delay(1500)

