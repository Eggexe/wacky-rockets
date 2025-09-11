#from PhysicsEngine import PhysicsEngine
#from RocketClass import Rocket
import pygame
#import pygamegui
#import sys


# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wacky Rockets")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    screen.fill((30, 30, 30))  # Dark gray background

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
