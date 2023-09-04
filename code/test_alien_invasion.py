import unittest
from settings import Settings
import pygame
from ship import Ship
from alien_invasion import AlienInvasion


class TestAlienInvasion(unittest.TestCase):
    """Test for the class AlienInvation"""

    def setUp(self):
        """create a set of response for use in all test methods"""
        pygame.init()
        self.settings = Settings()

        # make screen to the test
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.images = []

    def test_ship_index_start_empty(self):
        """Test that the index is empty"""
        self.assertEqual(self.ship.index, 0)

    def test_all_images_append_to_sprite_array_correctly(self):
        """test that all images is appended correctly to sprite array"""
        self.images.append(pygame.image.load('../game_assets/ship_1.bmp'))
        self.images.append(pygame.image.load('../game_assets/ship_2.bmp'))
        self.images.append(pygame.image.load('../game_assets/ship_3.bmp'))
        self.assertIn(self.images[0], self.images)
        self.assertIn(self.images[1], self.images)
        self.assertIn(self.images[2], self.images)
