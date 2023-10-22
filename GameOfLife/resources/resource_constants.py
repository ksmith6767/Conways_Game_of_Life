from typing import Final, Tuple


class ResourceConstants:

    # References for fonts
    EIGHT_BIT_WONDER_FONT: Final[str] = 'resources/8-BIT WONDER.TTF'
    PIXEBOY_FONT: Final[str] = 'resources/Pixeboy-z8XGD.ttf'

    # Color definitions
    GREY: Final[Tuple] = (50, 50, 50)
    LIGHT_GREY: Final[Tuple] = (70, 70, 70)
    BLUE: Final[Tuple] = (0, 50, 205)
    LIGHTBLUE: Final[Tuple] = (0, 70, 225)
    LIGHT_BLACK: Final[Tuple] = (30, 30, 30)
    RED: Final[Tuple] = (255, 0, 0)
    GREEN: Final[Tuple] = (0, 255, 0)
    PURPLE: Final[Tuple] = (255, 0, 255)
    ORANGE: Final[Tuple] = (255, 169, 0)
    WHITE: Final[Tuple] = (255, 255, 255)
    BLACK: Final[Tuple] = (0, 0, 0)

    # Number of cells for width and height of a board
    CELLS_WIDE: Final[int] = 25
    CELLS_TALL: Final[int] = 25

    # Starting cell rules
    LIVE_RULE_1: Final[int] = 2
    LIVE_RULE_2: Final[int] = 3
    DEAD_RULE: Final[int] = 3


