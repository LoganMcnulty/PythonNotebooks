import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets"""
    def __init__(self, pp_settings, screen, ship):
        """Create bullet object at ship's current position"""
        super().__init__()
        self.screen = screen
        
        # create a bullet rect at (0,0) and set current position
        self.rect = pygame.Rect(0, 0, pp_settings.bullet_width, pp_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # store bullet position as decimal value
        self.y = float(self.rect.y)
        
        self.color = pp_settings.bullet_color
        self.speed_factor = pp_settings.bullet_speed_factor
        
def update(self):
    """move bullet up the screen"""
    # update the decimal position of the bullet.
    self.y -= self.speed_factor
    
    # update rect position
    self.rect.y = self.y
    
def draw_bullet(self):
    """draw bullet to the screen"""
    pygame.draw.rect(self.screen, self.color, self.rect)