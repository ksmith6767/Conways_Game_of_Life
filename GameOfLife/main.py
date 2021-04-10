
from GameOfLife.Board import Board

from GameOfLife.Button import Button

import pygame

pygame.init()

# define the screen as 500X500 pixels
(width, height) = (750, 750)
screen = pygame.display.set_mode((width, height))

# color definitions
GREY = (50, 50, 50)
LIGHTGREY = (70, 70, 70)
BLUE = (0, 50, 205)
LIGHTBLUE = (0, 70, 225)

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

# repopulate button
newbutton = Button(GREY, 25, 525, 200, 50, 'Repopulate')
# step button
newbutton2 = Button(GREY, 300, 525, 200, 50, 'Step')
# clear button
newbutton3 = Button(GREY, 25, 600, 200, 50, 'Clear')



# MAIN GAME LOOP
run = True
while run:

    screen.fill((35, 35, 35))

    newbutton.draw(screen)
    newbutton2.draw(screen)
    newbutton3.draw(screen)


    # block to draw the representation of the board
    for i in range(WIDTH):
        for j in range(HEIGHT):

            if board.getCell(i, j).getStatus():
                switch = BLUE
            else:
                switch = GREY

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

        if event.type == pygame.MOUSEMOTION:
            if newbutton.over(pygame.mouse.get_pos()):
                newbutton.color = LIGHTGREY
            else:
                newbutton.color = GREY

            if newbutton2.over(pygame.mouse.get_pos()):
                newbutton2.color = LIGHTGREY
            else:
                newbutton2.color = GREY

            if newbutton3.over(pygame.mouse.get_pos()):
                newbutton3.color = LIGHTGREY
            else:
                newbutton3.color = GREY



        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            mouse_pos = event.pos
            if x < 500 and y < 500:
                print(x, y)
                x = int(x/20)
                y = int(y/20)
                print(x, y)
                if not board.getCell(x, y).getStatus():
                    board.getCell(x, y).setStatus(True)
                else:
                    board.getCell(x, y).setStatus(False)
            # button collision for random population
            if newbutton.over(mouse_pos):
                print("ahhhh")
                board.populateBoard()
            # button collision for stepping
            if newbutton2.over(mouse_pos):
                for i in range(WIDTH):
                    for j in range(HEIGHT):
                        board1.getCell(i, j).setStatus(board.checkNeighbors(i, j))
                for i in range(WIDTH):
                    for j in range(HEIGHT):
                        board.getCell(i, j).setStatus(board1.getCell(i, j).getStatus())

            # button collision for clearing the board
            if newbutton3.over(mouse_pos):
                print("ahhhh")
                board.clear()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("press r")
                board.populateBoard()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                board.clear()

    pygame.time.delay(10)
