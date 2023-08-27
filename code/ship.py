import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # add all the image to sprite array
        self.images = []
        self.images.append(pygame.image.load('../game_assets/ship_1.bmp'))
        self.images.append(pygame.image.load('../game_assets/ship_2.bmp'))
        self.images.append(pygame.image.load('../game_assets/ship_3.bmp'))

        # index value to get the image from array
        # initially/in the beginning it is 0
        self.index = 0

        # now the image we will display will be the index from the image array.
        self.image = self.images[self.index]

        # creating a rect at position x,y (430, 545)
        # of size (48, 48) which is the size of sprite/image
        self.rect = pygame.Rect(430, 545, 41, 46)

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag to move the ship
        self.moving_right = False
        self.moving_left = False

    def update_ship_sprite(self):
        """When the update method is called, we will increment the index."""
        self.index += 1

        # if the index is larger than total images
        if self.index >= len(self.images):
            # we will change the index to 0 again
            self.index = 0

        # update the image we will display
        self.image = self.images[self.index]

    def update_ship_position(self):
        """Update the ship's position based on the movement flag"""
        # update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

    # Update rect object from self.x
        self.rect.x = self.x

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
