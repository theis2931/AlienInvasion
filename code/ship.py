import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('game_assets/space_ship_1.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottem center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
