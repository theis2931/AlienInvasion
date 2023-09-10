import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Initialise the frame timing clock.
        self.clock = pygame.time.Clock()

        # The self argument here refers to the current instance of
        # AlienInvasion. This parameter that gives ship access to the game
        self.Ship = Ship(self)

        # creating a group with the sprites to ship animation
        # ? where is this in use?
        self.ship_group = pygame.sprite.Group()

        # https://www.pygame.org/docs/ref/sprite.html
        self.Bullets = pygame.sprite.Group()

        # creating a group to handle all the aliens.
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_frame_time()
            self._update_ship()
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

    def _update_ship(self):
        """update ship sprites, and the ship position to the screen."""
        self.Ship.update_ship_sprite()
        self.Ship.update_ship_position()

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

    def _update_frame_time(self):
        """Use pygame.time.Clock.tick() to slow down to given framerate."""
        self.clock.tick(self.settings.fps)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # make an alien and find the number of aliens in a row.
        # spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fit on the screen.
        ship_height = self.Ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """update image on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        # draw the ships rect on the screen
        # pygame.draw.rect(self.screen, (250, 0, 250), self.Ship.rect)
        # draw the spaceship
        self.Ship.blit_me()
        # draw bullets to the screen
        for bullet in self.Bullets.sprites():
            bullet.blit_bullet()
        # draw each element in the group alien
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
