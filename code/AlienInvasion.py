import sys
import pygame

from Settings import Settings
from Ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.Settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.Settings.screen_width, self.Settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # The self argument here refers to the current instance of
        # AlienInvasion. This parameter that gives ship access to the game
        self.Ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """update image on the screen, and flip to the new screen."""
        self.screen.fill(self.Settings.bg_color)
        self.Ship.blit_me()

        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
