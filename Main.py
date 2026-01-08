import pygame
import sys
from RocketClass import RocketClass
from PhysicsEngine import PhysicsEngine

#basic instantiation
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wacky Rockets")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# game states - prevents weird logic from occuring
# e.g. game running while in a menu
MENU = "menu"
GAME = "game"
state = MENU

# making objects, NTPF and Fl2 used as testing fuels for proof of concept
rocket = RocketClass("NTPF", "Flourine")
physics = PhysicsEngine()

# button variables for instantiating later
start_btn = pygame.Rect(300, 250, 200, 50)
quit_btn = pygame.Rect(300, 320, 200, 50)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == MENU and event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn.collidepoint(event.pos):
                state = GAME
            if quit_btn.collidepoint(event.pos):
                running = False

    screen.fill((20, 20, 30))

    # MENU code for running the menu
    if state == MENU:
        # init buttons "start" + "quit"
        
        pygame.draw.rect(screen, (60, 120, 200), start_btn)
        pygame.draw.rect(screen, (200, 60, 60), quit_btn)

        screen.blit(font.render("START", True, (255, 255, 255)), (360, 265))
        screen.blit(font.render("QUIT", True, (255, 255, 255)), (370, 335))
        screen.blit(font.render("WACKY ROCKETS", True, (255, 255, 255)), (280, 150))

    # game code here
    pygame.display.flip()
    print(state)
    

    
pygame.quit()
sys.exit()
