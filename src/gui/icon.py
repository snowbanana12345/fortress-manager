import pygame
from src.gui.square_box import SquareBox

class Icon(SquareBox):
    def __init__(self, xpos, ypos, xlength, ylength, pygame_image):
        super().__init__(xpos, ypos, xlength, ylength)
        self.image = pygame_image
        self.image = pygame.transform.smoothscale(self.image, (xlength, ylength))

    def render(self, surface):
        super().render(surface)
        surface.blit(self.image, (self.xpos, self.ypos))







