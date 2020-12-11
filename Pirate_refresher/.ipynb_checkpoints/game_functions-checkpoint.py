# +
import sys
import pygame
from bullet import Bullet
from pirate import Pirate

def check_keydown_events(event, pp_settings, screen, ship, bullets):
# respond to key presses
    if event.key == pygame.K_d:
    # move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True 
    # fire bullets
    elif event.key == pygame.K_j:
        fire_bullet(pp_settings, screen, ship, bullets)
        
    elif event.key == pygame.K_ESCAPE:
        print('escape')
        pp_settings.running = False
    
            
def fire_bullet(pp_settings, screen, ship, bullets):
    # create a new bullet, and add it to the bullets group
    new_bullet = Bullet(pp_settings, screen, ship)
    if len(bullets) < pp_settings.bullets_allowed:
        bullets.add(new_bullet)
        
        
def check_keyup_events(event, ship):
# respond to key releases
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False

        
def check_events(pp_settings, screen, ship, bullets):
    # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, pp_settings, screen, ship, bullets)
                
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)

                    
def update_screen(pp_settings, screen, ship, pirates, bullets):
        """Update images on the screen, and flip to the new screen"""
    #redraw the screen during each pass thru the loop
        screen.fill(pp_settings.bg_color)
        ship.blitme()
        pirates.draw(screen)
        
    # redraw all bullets behind ship and aliens.
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
    # make the most recently drawn screen visible
        pygame.display.flip()
        
def update_bullets(bullets):
# update position of bullets, and get ride of old bullets.
#update bullet positions
    bullets.update()
# get ride of bullets that have gone above 0 x-axis (i.e. top of screen)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
def create_fleet(pp_settings, screen, pirates):
# create a full fleet of pirates
# create a pirate and find the number of pirates in a row
# spacing between each pirate is equal to one pirate width.
    pirate = Pirate(pp_settings, screen)
    pirate_width = pirate.rect.width
    available_space_x = pp_settings.screen_width -2 * pirate_width
    number_pirates_x = int(available_space_x / (2 * pirate_width))
    
# create first row of pirates
    for pirate_number in range(number_pirates_x):
    # create pirate, place in the row
        pirate = Pirate(pp_settings, screen)
        pirate.x = pirate_width + 2 * pirate_width * pirate_number
        pirate.rect.x = pirate.x
        pirates.add(pirate)

