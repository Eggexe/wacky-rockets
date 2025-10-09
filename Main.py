from PhysicsEngine import PhysicsEngine
from RocketClass import Rocket
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wacky Rockets")

# Create physics engine and rocket - TEMP, SWITCH TO USER CONTROL EVENTUALLY
engine = PhysicsEngine()
rocket = Rocket("Kerosene", "RP-1", "Liquid Oxygen")

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # Background

    # TEMP: print rocket fuel efficiency to console
    print(f"Fuel efficiency: {rocket.fuelEfficiency}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
