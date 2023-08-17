import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('../game_assets/ship_1.bmp')
        self.rect = self.image.get_rect()
        print(self.image.get_rect())

        # scale the image to fit the screen.
        # todo need to place the ship in the middle scale issue?
        # self.image = pygame.transform.scale(
        #     self.image, self.settings.default_image_size)

        # Start each new ship at the bottem center of the screen.
        # self.default_image_position = self.screen_rect
        # self.rect.midbottom = self.screen_rect.midbottom

        # Set the rockets start position.
        self.rect.x = 430
        self.rect.y = 545
        self.start_position = (self.rect.x, self.rect.y)

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # todo line 39 stop before the corner then scale activated
        # update the ship's x position, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
