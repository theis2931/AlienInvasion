import unittest
from settings import Settings
import pygame
from ship import Ship
from alien_invasion import AlienInvasion


class TestAlienInvasion(unittest.TestCase):
    """Test for the class AlienInvasion"""

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

        # index value to get the image from array
        # initially/in the beginning it is 0
        self.index = 0

        # creating a group with the sprites to ship animation
        self.ship_group = pygame.sprite.Group()

        # https://www.pygame.org/docs/ref/sprite.html
        self.Bullets = pygame.sprite.Group()

    # test for the spaceship
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

    def test_ship_animation_index_is_increasing(self):
        """
        test that the index is increasing.
        """
        self.images.append(pygame.image.load('../game_assets/ship_1.bmp'))
        self.images.append(pygame.image.load('../game_assets/ship_2.bmp'))
        self.images.append(pygame.image.load('../game_assets/ship_3.bmp'))
        self.ship.index += 1

        self.assertLess(0, self.ship.index)

    def test_index_reset_to_0_if_index_larger_than_sprites(self):
        """
        test that the index change index to 0 if index larger than total image
        """
        self.images.append(pygame.image.load('../game_assets/ship_1.bmp'))
        self.images.append(pygame.image.load('../game_assets/ship_2.bmp'))
        self.index = 3

        # if the index is larger than total images
        if self.index >= len(self.images):
            # we will change the index to 0 again
            self.index = 0

        self.assertEqual(0, self.ship.index)


if __name__ == '__main__':
    unittest.main()
