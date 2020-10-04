import sys
import pygame

def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_d:
        ship.moving_right = True
        
    elif event.key == pygame.K_a:
        ship.moving_left = True
        
def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_d:
        ship.moving_right = False
        
    elif event.key == pygame.K_a:
        ship.moving_left = False

def check_events(ship):
    """respond to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
                
        elif event.type == pygame.KEYUP:
            check_keydown_event(event, ship)
            
def update_screen(pp_settings, screen, ship):
# redraw screen during each passthrough loop
    screen.fill(pp_settings.bg_color)
    ship.blitme()

# make most recently drawn screen visible.
    pygame.display.flip()