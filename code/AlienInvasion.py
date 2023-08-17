import sys
import pygame

from Settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # The self argument here refers to the current instance of
        # AlienInvasion. This parameter that gives ship access to the game
        self.Ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.Ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keypress_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keypress_events(self, event):
        """Response to key presses."""
        if event.key == pygame.K_RIGHT:
            self.Ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.Ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Response to key releases."""
        if event.key == pygame.K_RIGHT:
            self.Ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.Ship.moving_left = False

    def _update_screen(self):
        """update image on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        # draw rect on the screen
        # pygame.draw.rect(self.screen, (250, 0, 250), self.Ship.rect)

        # draw the spaceship
        self.Ship.blit_me()

        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
