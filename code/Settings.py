class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialize the game's settings."""
        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (229, 204, 255)
        self.default_image_size = (30, 30)  # set the size of the image
        # Ship settings
        self.ship_speed = 1.5
        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
