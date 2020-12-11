# +
class Settings():
    
# a class to store all settings for Pirate Patrol

    def __init__(self):
        """ initialize game settings"""
    # screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (52, 146, 235)
        
    # Ship settings
        self.ship_speed_factor = 1.5
        
    # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.running = True
# -




