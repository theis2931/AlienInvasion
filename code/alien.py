import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        # special function that allow you to call from the parrent class Sprite
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('../game_assets/alien_blue_1.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)



