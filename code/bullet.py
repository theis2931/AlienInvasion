import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """
        create a bullet object at the ship's current position,
        and call super() to inherit properly from Sprite.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the bullet image, and set the bullet position.
        self.image = pygame.image.load('../game_assets/firebullet_purple.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.Ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def blit_bullet(self):
        """Draw the bullet at the current position."""
        self.screen.blit(self.image, self.rect)
