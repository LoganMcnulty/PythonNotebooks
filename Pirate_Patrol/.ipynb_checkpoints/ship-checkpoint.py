import pygame

class Ship():
    def __init__(self, pp_settings, screen):
        """Initialize ship, set starting position"""
        self.screen = screen
        self.pp_settings = pp_settings
        
    # Load ship image and get its rect.
        self.image = pygame.image.load('images/BlackSail/N_PShip_BMP_110x110.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
    # Start ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
    # Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """update ships position based on movement flag """
        if self.moving_right and self.rect.right < self.screen_rect.right:
    # update the ship's center value, not the rect.
            self.center += self.pp_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.pp_settings.ship_speed_factor
            
    # update the center value
        self.rect.centerx = self.center
        
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)