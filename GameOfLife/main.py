from typing import List, Tuple

import pygame

from GameOfLife.resources.resource_constants import ResourceConstants

from GameOfLife.util.logic_util import LogicUtil

from GameOfLife.Board import Board
from GameOfLife.Button import Button
from GameOfLife.util.render_util import RenderUtil


def get_screen(width: int, height: int):
    (width, height) = (750, 750)
    return pygame.display.set_mode((width, height))


def evaluate_button_highlighting(buttons: List[Button], mouse_pos: Tuple[float, float]):
    for button in buttons:
        if button.over(mouse_pos):
            button.color = button.highlight_color
        else:
            button.color = button.primary_color


pygame.init()
clock = pygame.time.Clock()


# Define the screen dimensions
screen = get_screen(750, 750)

# define original cell rules
live_rule_1 = ResourceConstants.LIVE_RULE_1
live_rule_2 = ResourceConstants.LIVE_RULE_2
dead_rule = ResourceConstants.DEAD_RULE

# create new board and temp board for updating purposes
game_used_board = Board(ResourceConstants.CELLS_WIDE, ResourceConstants.CELLS_TALL, live_rule_1, live_rule_2, dead_rule)
game_placeholder_board = Board(ResourceConstants.CELLS_WIDE, ResourceConstants.CELLS_TALL,
                               live_rule_1, live_rule_2, dead_rule)
game_used_board.populateBoard()
game_placeholder_board.clear()

# create new board and temp board for menu screen
menu_used_board = Board(ResourceConstants.CELLS_WIDE, ResourceConstants.CELLS_TALL, 2, 3, 3)
menu_placeholder_board = Board(ResourceConstants.CELLS_WIDE, ResourceConstants.CELLS_TALL, 2, 3, 3)
menu_used_board.populateBoard()
menu_placeholder_board.clear()

# Create a list of buttons in the main menu and game
buttons_in_game: List[Button] = []
buttons_in_main_menu: List[Button] = []

# Instantiate highlightable buttons
repopulate_button = Button(ResourceConstants.GREY, 25, 525, 200, 75, 'Random')
buttons_in_game.append(repopulate_button)
step_button = Button(ResourceConstants.GREY, 300, 525, 200, 75, 'Step')
buttons_in_game.append(step_button)
clear_button = Button(ResourceConstants.GREY, 25, 625, 200, 75, 'Clear')
buttons_in_game.append(clear_button)
start_game_button = Button(ResourceConstants.LIGHT_BLACK, 275, 425, 200, 50, 'Start')
buttons_in_main_menu.append(start_game_button)
menu_button = Button(ResourceConstants.GREY, 300, 625, 200, 75, 'Menu')
buttons_in_game.append(menu_button)

# Live rule 1 buttons
live_rule_1_incrementer = Button(ResourceConstants.GREY, 525, 15 + 30, 200, 20, '+')
buttons_in_game.append(live_rule_1_incrementer)
live_rule_1_button = Button(ResourceConstants.GREY, 525, 45 + 30, 200, 75, str(live_rule_1),
                            highlight_color=ResourceConstants.GREY)
buttons_in_game.append(live_rule_1_button)
live_rule_1_decrementer = Button(ResourceConstants.GREY, 525, 130 + 30, 200, 20, '-')
buttons_in_game.append(live_rule_1_decrementer)

# Live rule 2 buttons
live_rule_2_incrementer = Button(ResourceConstants.GREY, 525, 165 + 30, 200, 20, '+')
buttons_in_game.append(live_rule_2_incrementer)
live_rule_2_button = Button(ResourceConstants.GREY, 525, 195 + 30, 200, 75, str(live_rule_2),
                            highlight_color=ResourceConstants.GREY)
buttons_in_game.append(live_rule_2_button)
live_rule_2_decrementer = Button(ResourceConstants.GREY, 525, 280 + 30, 200, 20, '-')
buttons_in_game.append(live_rule_2_decrementer)

# Dead rule Buttons
dead_rule_incrementer = Button(ResourceConstants.GREY, 525, 375, 200, 20, '+')
buttons_in_game.append(dead_rule_incrementer)
dead_rule_button = Button(ResourceConstants.GREY, 525, 405, 200, 75, str(dead_rule),
                          highlight_color=ResourceConstants.GREY)
buttons_in_game.append(dead_rule_button)
dead_rule_decrementer = Button(ResourceConstants.GREY, 525, 490, 200, 20, '-')
buttons_in_game.append(dead_rule_decrementer)


player_color = ResourceConstants.PURPLE

# Color settings buttons
red = Button(ResourceConstants.RED, 235, 525, 75, 75, '',
             ResourceConstants.RED, ResourceConstants.RED)
red_border = Button(ResourceConstants.RED, 230, 520, 85, 85, '',
                    ResourceConstants.RED, ResourceConstants.WHITE)
green = Button(ResourceConstants.GREEN, 335, 525, 75, 75, '',
               ResourceConstants.GREEN, ResourceConstants.GREEN)
green_border = Button(ResourceConstants.GREEN, 330, 520, 85, 85, '',
                      ResourceConstants.GREEN, ResourceConstants.WHITE)
purple = Button(ResourceConstants.PURPLE, 435, 525, 75, 75, '',
                ResourceConstants.PURPLE, ResourceConstants.PURPLE)
purple_border = Button(ResourceConstants.PURPLE, 430, 520, 85, 85, '',
                       ResourceConstants.PURPLE, ResourceConstants.WHITE)
blue = Button(ResourceConstants.BLUE, 275, 625, 75, 75, '',
              ResourceConstants.BLUE, ResourceConstants.BLUE)
blue_border = Button(ResourceConstants.BLUE, 270, 620, 85, 85, '',
                     ResourceConstants.BLUE, ResourceConstants.WHITE)
orange = Button(ResourceConstants.ORANGE, 400, 625, 75, 75, '',
                ResourceConstants.ORANGE, ResourceConstants.ORANGE)
orange_border = Button(ResourceConstants.ORANGE, 395, 620, 85, 85, '',
                       ResourceConstants.ORANGE, ResourceConstants.WHITE)

buttons_in_main_menu.append(red_border)
buttons_in_main_menu.append(green_border)
buttons_in_main_menu.append(purple_border)
buttons_in_main_menu.append(blue_border)
buttons_in_main_menu.append(orange_border)

buttons_in_main_menu.append(red)
buttons_in_main_menu.append(green)
buttons_in_main_menu.append(purple)
buttons_in_main_menu.append(blue)
buttons_in_main_menu.append(orange)

# Main loop variables
run = True
menu_run = True
while run:

    # Main-Menu loop begin *********************************************************************************************
    while menu_run:

        RenderUtil.render_menu_board(screen, menu_used_board, player_color)
        for button in buttons_in_main_menu:
            button.draw(screen)

        font = pygame.font.Font(ResourceConstants.EIGHT_BIT_WONDER_FONT, 50)
        text = font.render('Game of Life', 1, (255, 255, 255))
        screen.blit(text, (375-text.get_width()/2, 200))

        pygame.display.update()
        pygame.time.delay(10)

        if pygame.time.get_ticks() % 100 == 0:
            LogicUtil.update_board(menu_used_board, menu_placeholder_board)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                menu_run = False
                run = False

            if event.type == pygame.MOUSEMOTION:
                evaluate_button_highlighting(buttons_in_main_menu, pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = event.pos
                if start_game_button.over(mouse_pos):
                    run = True
                    menu_run = False
                    start_game_button.color = ResourceConstants.LIGHT_BLACK
                if purple.over(mouse_pos):
                    player_color = ResourceConstants.PURPLE
                if blue.over(mouse_pos):
                    player_color = ResourceConstants.BLUE
                if orange.over(mouse_pos):
                    player_color = ResourceConstants.ORANGE
                if red.over(mouse_pos):
                    player_color = ResourceConstants.RED
                if green.over(mouse_pos):
                    player_color = ResourceConstants.GREEN

    # Main-Menu loop end ***********************************************************************************************

    screen.fill((35, 35, 35))
    for button in buttons_in_game:
        button.draw(screen)

    font = pygame.font.Font(ResourceConstants.EIGHT_BIT_WONDER_FONT, 20)
    text = font.render('Live Rules', 1, (255, 255, 255))
    screen.blit(text, (625 - text.get_width() / 2, 15))

    font = pygame.font.Font(ResourceConstants.EIGHT_BIT_WONDER_FONT, 20)
    text = font.render('Dead Rule', 1, (255, 255, 255))
    screen.blit(text, (625 - text.get_width() / 2, 345))

    font = pygame.font.Font(ResourceConstants.EIGHT_BIT_WONDER_FONT, 20)
    text = font.render('Revived', 1, (255, 255, 255))
    screen.blit(text, (625 - text.get_width() / 2, 525))

    font = pygame.font.Font(ResourceConstants.EIGHT_BIT_WONDER_FONT, 35)
    text = font.render(str(game_used_board.getRevived()), 1, (255, 255, 255))
    screen.blit(text, (625 - text.get_width() / 2, 555))

    font = pygame.font.Font(ResourceConstants.EIGHT_BIT_WONDER_FONT, 20)
    text = font.render('Killed', 1, (255, 255, 255))
    screen.blit(text, (625 - text.get_width() / 2, 625))

    font = pygame.font.Font(ResourceConstants.EIGHT_BIT_WONDER_FONT, 35)
    text = font.render(str(game_used_board.getKilled()), 1, (255, 255, 255))
    screen.blit(text, (625 - text.get_width() / 2, 655))

    # block to draw the representation of the board
    for i in range(ResourceConstants.CELLS_WIDE):
        for j in range(ResourceConstants.CELLS_TALL):

            if game_used_board.getCell(i, j).getStatus():
                pygame.draw.rect(screen, player_color, (i * 20, j * 20, 18, 18))
            else:
                pygame.draw.rect(screen, ResourceConstants.GREY, (i * 20, j * 20, 18, 18))

    pygame.display.update()

    # Process user-input in the game loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(ResourceConstants.CELLS_WIDE):
                    for j in range(ResourceConstants.CELLS_TALL):
                        game_placeholder_board.getCell(i, j).setStatus(game_used_board.checkNeighbors(i, j))
                for i in range(ResourceConstants.CELLS_WIDE):
                    for j in range(ResourceConstants.CELLS_TALL):
                        game_used_board.getCell(i, j).setStatus(game_placeholder_board.getCell(i, j).getStatus())

        if event.type == pygame.MOUSEMOTION:
            evaluate_button_highlighting(buttons_in_game, pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            mouse_pos = event.pos
            if x < 500 and y < 500:
                print(x, y)
                x = int(x/20)
                y = int(y/20)
                print(x, y)
                if not game_used_board.getCell(x, y).getStatus():
                    game_used_board.getCell(x, y).setStatus(True)
                else:
                    game_used_board.getCell(x, y).setStatus(False)
            # button collision for random population
            if repopulate_button.over(mouse_pos):
                print("ahhhh")
                game_used_board.populateBoard()
            # button collision for stepping
            if step_button.over(mouse_pos):
                LogicUtil.update_board(game_used_board, game_placeholder_board)

            # button collision for clearing the board
            if clear_button.over(mouse_pos):
                print("ahhhh")
                game_used_board.clear()

            if menu_button.over(mouse_pos):
                menu_run = True

            if live_rule_1_incrementer.over(mouse_pos):
                live_rule_1 += 1
                live_rule_1_button.text = str(live_rule_1)
                game_used_board.liverule1 = live_rule_1

            if live_rule_1_decrementer.over(mouse_pos):
                live_rule_1 -= 1
                live_rule_1_button.text = str(live_rule_1)
                game_used_board.liverule1 = live_rule_1

            if live_rule_2_incrementer.over(mouse_pos):
                live_rule_2 += 1
                live_rule_2_button.text = str(live_rule_2)
                game_used_board.liverule2 = live_rule_2

            if live_rule_2_decrementer.over(mouse_pos):
                live_rule_2 -= 1
                live_rule_2_button.text = str(live_rule_2)
                game_used_board.liverule2 = live_rule_2

            if dead_rule_incrementer.over(mouse_pos):
                dead_rule += 1
                dead_rule_button.text = str(dead_rule)
                game_used_board.deadrule = dead_rule

            if dead_rule_decrementer.over(mouse_pos):
                dead_rule -= 1
                dead_rule_button.text = str(dead_rule)
                game_used_board.deadrule = dead_rule

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("press r")
                game_used_board.populateBoard()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                game_used_board.clear()

    pygame.time.delay(10)
