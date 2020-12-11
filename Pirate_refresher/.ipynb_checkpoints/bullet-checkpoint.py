# +
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
# Class to manage bullets fired from the ship
    def __init__(self, pp_settings, screen, ship):
    # Create bullet object at ship's current position
        super(Bullet, self).__init__()
        self.screen = screen
        
    # create a bullet rect at (0, 0), and then set correct position
        self.rect = pygame.Rect(0, 0, pp_settings.bullet_width, pp_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
    # store ship's position as decimal value
        self.y = float(self.rect.y)
        self.color = pp_settings.bullet_color
        self.speed_factor = pp_settings.bullet_speed_factor
        
    def update(self):
    # move bullets up the screen
    # update the decimal position of the bullet
        self.y -= self.speed_factor
    # update the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
    # draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    
        
        
