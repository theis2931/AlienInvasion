class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (229, 204, 255)
        self.default_image_size = (60, 60)  # set the size of the image
        # Ship settings
        self.ship_speed = 0.5
