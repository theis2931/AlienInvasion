class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialize the game's settings."""
        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.default_image_size = (30, 30)  # set the size of the image
        self.fps = 25
        # Ship settings
        self.ship_speed = 6.5
        # bullet settings
        self.bullet_speed = 6.6
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

