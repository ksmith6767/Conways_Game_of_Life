
from GameOfLife.Board import Board

from GameOfLife.Button import Button

import pygame

pygame.init()

# define the screen as 500X500 pixels
(width, height) = (750, 750)
screen = pygame.display.set_mode((width, height))

# define original cell rules
liverule1 = 2
liverule2 = 3
deadrule = 3

# color definitions
GREY = (50, 50, 50)
LIGHTGREY = (70, 70, 70)
BLUE = (0, 50, 205)
LIGHTBLUE = (0, 70, 225)
BLACK = (30, 30, 30)

# define the bounds of the board for game
WIDTH = 25
HEIGHT = 25

# switcher variable for cell colors
switch = BLUE

clock = pygame.time.Clock()

# create new board and temp board for updating purposes
board = Board(WIDTH, HEIGHT, liverule1, liverule2, deadrule)
board1 = Board(WIDTH, HEIGHT, liverule1, liverule2, deadrule)

# create new board and temp board for menu screen
board2 = Board(WIDTH, HEIGHT, 2, 3, 3)
board3 = Board(WIDTH, HEIGHT, 2, 3, 3)

# initialize game boards
board.populateBoard()
board1.clear()

# initialize menu boards
board2.populateBoard()
board3.clear()

# repopulate button
newbutton = Button(GREY, 25, 525, 200, 75, 'Random')
# step button
newbutton2 = Button(GREY, 300, 525, 200, 75, 'Step')
# clear button
newbutton3 = Button(GREY, 25, 625, 200, 75, 'Clear')

# start game button
newbutton4 = Button(BLACK, 275, 425, 200, 50, 'Start')

# menu button
newbutton5 = Button(GREY, 300, 625, 200, 75, 'Menu')

# *** liverule 1 buttons

# top scroll button
newbutton6 = Button(GREY, 525, 15+30, 200, 20, '')
#  button
newbutton7 = Button(GREY, 525, 45+30, 200, 75, str(liverule1))
# bottom scroll button
newbutton8 = Button(GREY, 525, 130+30, 200, 20, '')

# *** liverule 2 buttons

# top scroll button
newbutton9 = Button(GREY, 525, 165+30, 200, 20, '')
#  button
newbutton10 = Button(GREY, 525, 195+30, 200, 75, str(liverule2))
# bottom scroll button
newbutton11 = Button(GREY, 525, 280+30, 200, 20, '')



#menu loop
run = True
menurun = True



# MAIN GAME LOOP

while run:

    while menurun:
        screen.fill((35, 35, 35))

        # block to draw the representation of the board
        for i in range(WIDTH):
            for j in range(HEIGHT):

                if board2.getCell(i, j).getStatus():
                    switch = BLUE
                else:
                    switch = GREY

                pygame.draw.rect(screen, switch, (i * 30, j * 30, 28, 28))

        newbutton4.draw(screen)

        font = pygame.font.Font('GameOfLife/8-BIT WONDER.TTF', 50)
        text = font.render('Game of Life', 1, (255, 255, 255))
        screen.blit(text, (375-text.get_width()/2, 200))

        pygame.display.update()
        pygame.time.delay(10)

        if pygame.time.get_ticks() % 100 == 0:
            print("asdf")
            for i in range(WIDTH):
                for j in range(HEIGHT):
                    board3.getCell(i, j).setStatus(board2.checkNeighbors(i, j))
            for i in range(WIDTH):
                for j in range(HEIGHT):
                    board2.getCell(i, j).setStatus(board3.getCell(i, j).getStatus())

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                menurun = False
                run = False

            if event.type == pygame.MOUSEMOTION:
                if newbutton4.over(pygame.mouse.get_pos()):
                    newbutton4.color = LIGHTGREY
                else:
                    newbutton4.color = BLACK

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = event.pos
                if newbutton4.over(mouse_pos):
                    run = True
                    menurun = False
                    newbutton4.color = BLACK

    screen.fill((35, 35, 35))

    newbutton.draw(screen)
    newbutton2.draw(screen)
    newbutton3.draw(screen)
    newbutton5.draw(screen)
    newbutton6.draw(screen)
    newbutton7.draw(screen)
    newbutton8.draw(screen)
    newbutton9.draw(screen)
    newbutton10.draw(screen)
    newbutton11.draw(screen)

    font = pygame.font.Font('GameOfLife/8-BIT WONDER.TTF', 20)
    text = font.render('Live Rules', 1, (255, 255, 255))
    screen.blit(text, (625 - text.get_width() / 2, 15))

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
            if newbutton5.over(pygame.mouse.get_pos()):
                newbutton5.color = LIGHTGREY
            else:
                newbutton6.color = GREY
            if newbutton6.over(pygame.mouse.get_pos()):
                newbutton6.color = LIGHTGREY

            else:
                newbutton8.color = GREY
            if newbutton8.over(pygame.mouse.get_pos()):
                newbutton8.color = LIGHTGREY
            else:
                newbutton8.color = GREY



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

            if newbutton5.over(mouse_pos):
                menurun = True

            if newbutton6.over(mouse_pos):
                liverule1 += 1
                newbutton7.text = str(liverule1)
                board.liverule1 = liverule1

            if newbutton8.over(mouse_pos):
                liverule1 -= 1
                newbutton7.text = str(liverule1)
                board.liverule1 = liverule1


            if newbutton9.over(mouse_pos):
                liverule2 += 1
                newbutton10.text = str(liverule2)
                board.liverule2 = liverule2

            if newbutton11.over(mouse_pos):
                liverule2 -= 1
                newbutton10.text = str(liverule2)
                board.liverule2 = liverule2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("press r")
                board.populateBoard()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                board.clear()


    pygame.time.delay(10)
