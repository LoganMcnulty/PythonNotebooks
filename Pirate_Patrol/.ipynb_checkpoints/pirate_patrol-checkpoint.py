import sys 
import pygame

print("Welcome to Alien Invasion")

def run_game():
    # initialize game and create screen object
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    # start main loop for the game.
    while True:
        
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # make most recently drawn screen visible.
        pygame.display.flip()
        
run_game()