import pygame

from Settings import Settings


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.Settings = Settings()

        # load the ship image and get its rect.
        self.image = pygame.image.load('game_assets/space_ship_1.bmp')
        self.rect = self.image.get_rect()

        # scale the image to fit the screen
        # todo need to place the ship in the middle scale issue?
        self.image = pygame.transform.scale(
            self.image, self.Settings.default_image_size)

        # Start each new ship at the bottem center of the screen.
        self.default_image_position = self.screen_rect
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
