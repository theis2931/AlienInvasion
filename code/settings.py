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
        self.bullet_speed = 5.5
        self.bullets_allowed = 3
