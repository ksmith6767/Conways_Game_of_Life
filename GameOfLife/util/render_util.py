import pygame

from GameOfLife.resources.resource_constants import ResourceConstants


class RenderUtil:

    @staticmethod
    def render_menu_board(screen, board, player_color):
        screen.fill((35, 35, 35))

        for i in range(ResourceConstants.CELLS_WIDE):
            for j in range(ResourceConstants.CELLS_TALL):
                if board.getCell(i, j).getStatus():
                    pygame.draw.rect(screen, player_color, (i * 30, j * 30, 28, 28))
                else:
                    pygame.draw.rect(screen, ResourceConstants.GREY, (i * 30, j * 30, 28, 28))
