from GameOfLife.Board import Board
from GameOfLife.resources.resource_constants import ResourceConstants


class LogicUtil:

    @staticmethod
    def update_board(used_board: Board, placeholder_board: Board):
        for i in range(ResourceConstants.CELLS_WIDE):
            for j in range(ResourceConstants.CELLS_TALL):
                placeholder_board.getCell(i, j).setStatus(used_board.checkNeighbors(i, j))
        for i in range(ResourceConstants.CELLS_WIDE):
            for j in range(ResourceConstants.CELLS_TALL):
                used_board.getCell(i, j).setStatus(placeholder_board.getCell(i, j).getStatus())
