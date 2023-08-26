import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


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

        # https://www.pygame.org/docs/ref/sprite.html
        self.Bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.Ship.update()
            self._update_bullet()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Response to key releases."""
        if event.key == pygame.K_RIGHT:
            self.Ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.Ship.moving_left = False

    def _fire_bullet(self):
        """
        Create a new bullet, and add it to the bullets group.
        if it complies with bullets_allowed.
        """
        if len(self.Bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.Bullets.add(new_bullet)

    def _update_bullet(self):
        """Update position of bullet and get rid of old bullets."""
        # update bullet position
        self.Bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.Bullets.copy():
            if bullet.rect.bottom <= 0:
                self.Bullets.remove(bullet)
        # print(len(self.Bullets))

    def _update_screen(self):
        """update image on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        # draw rect on the screen
        # pygame.draw.rect(self.screen, (250, 0, 250), self.Ship.rect)
        # draw the spaceship
        self.Ship.blit_me()
        # draw bullets to the screen
        for bullet in self.Bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
