# +
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
# initialize game, create screen object
    pygame.init()
    pp_settings = Settings()
    screen = pygame.display.set_mode((pp_settings.screen_width, pp_settings.screen_height))
    pygame.display.set_caption("Pirate Patrol")
    
# make a ship, a group of bullets, and a group of enemies
    ship = Ship(pp_settings, screen)
    bullets = Group()
    pirates = Group()
    gf.create_fleet(pp_settings, screen, pirates)

# start main loop
    while pp_settings.running:
        gf.check_events(pp_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(pp_settings, screen, ship, pirates, bullets)
        
run_game()
