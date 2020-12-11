# +
import pygame
from pygame.sprite import Sprite

class Pirate(Sprite):
# class to represent a single alien in the fleet
    def __init__(self, pp_settings, screen):
    # initialize alien and set its starting position
        super(Pirate, self).__init__()
        self.screen = screen
        self.pp_settings = pp_settings
    # load alien image, set rect
        self.image = pygame.image.load('images/pirates/pirate_70x70.bmp')
        self.rect = self.image.get_rect()
    # new aliens at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    # store the alien's exact position.
        self.x = float(self.rect.x)
    
    def blitme(self):
    # draw alien at its current location
        self.screen.blit(self.image, self.rect)
