import pygame

from GameOfLife.resources.resource_constants import ResourceConstants


# Some of this code is based on a tutorial I found online for creating text buttons
class Button:
    WHITE = (255, 255, 255)

    def __init__(self, color, x, y, width, height, text, primary_color=ResourceConstants.GREY,
                 highlight_color=ResourceConstants.LIGHT_GREY):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        self.text = text
        self.highlight_color = highlight_color
        self.primary_color = primary_color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.Font('resources/Pixeboy-z8XGD.ttf', 35)
            text = font.render(self.text, 1, (255, 255, 255))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

