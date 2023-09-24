import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    """A class to represent a single alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        # special function that allow you to call from the parrent class Sprite
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('../game_assets/alien_blue_1.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edge(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x





