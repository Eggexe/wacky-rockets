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

rocket.y = HEIGHT - 60 # force rocket to be on landing pad
rocket.v_velocity = 0


# code added here to keep a list of the names, values and indexes of the fuel
# and oxidiser lists in RocketClass.py, needed to cleanly switch them properly
fuel_list = list(RocketClass.r_Fuels.keys())
oxidiser_list = list(RocketClass.r_Oxidiser.keys())
fuel_index = fuel_list.index(rocket.fuel1)
oxidiser_index = oxidiser_list.index(rocket.oxidiser1)

# button variables for instantiating later
start_btn = pygame.Rect(300, 250, 200, 50)
quit_btn = pygame.Rect(300, 320, 200, 50)

running = True
while running:
    dt = clock.tick(60) / 1000

    ######################## FUEL CHANGE HERE #####################

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and state == GAME:
        # fuel change L press
            if event.key == pygame.K_l:
                fuel_index = (fuel_index + 1) % len(fuel_list) # % prevents crash
                rocket.set_fuel(fuel_list[fuel_index])

            # oxidiser change K press
            if event.key == pygame.K_k:
                oxidiser_index = (oxidiser_index + 1) % len(oxidiser_list) # ^^^
                rocket.set_oxidiser(oxidiser_list[oxidiser_index])
        print(oxidiser_index)
        print(rocket.fuel1)
        print(rocket.oxidiser1)
        print(rocket.r_Fuels[fuel_list[fuel_index]])
        

    ###################### GAME CODE HEERE ###############################
        
        if state == GAME and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rocket.velocity = 100 * rocket.mass * physics.calculate_fuelEfficiency(rocket.r_Fuels[fuel_list[fuel_index]],rocket.r_Oxidiser[oxidiser_list[oxidiser_index]])

    ###################### QUIT THE GAME HERE ##############################
        
        if event.type == pygame.QUIT:
            running = False

        if state == MENU and event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn.collidepoint(event.pos):
                state = GAME
            if quit_btn.collidepoint(event.pos):
                running = False

    screen.fill((20, 20, 30))

    ################## MENU CODE HERE #########################
         

 
    # MENU code for running the menu
    if state == MENU:
        # init buttons "start" + "quit"
        
        pygame.draw.rect(screen, (60, 120, 200), start_btn)
        pygame.draw.rect(screen, (200, 60, 60), quit_btn)

        screen.blit(font.render("START", True, (255, 255, 255)), (360, 265))
        screen.blit(font.render("QUIT", True, (255, 255, 255)), (370, 335))
        screen.blit(font.render("WACKY ROCKETS", True, (255, 255, 255)), (280, 150))

   
    

    #establish text variables again, same with the START and QUIT buttons
    # except it should display data from the RocketClass
    if state == GAME:
        fuel_text = font.render(f"Fuel: {rocket.fuel1}", True, (255,255,255))
        oxidiser_test = font.render(f"Oxidiser: {rocket.oxidiser1}", True, (255,255,255))

        

        # send to screen and display from the width of the screen to a corner
        screen.blit(fuel_text, (WIDTH- fuel_text.get_width() - 20,20))
        screen.blit(oxidiser_test, (WIDTH- oxidiser_test.get_width() - 20,55))


    ############## LEVEL DRAWING PARTS ##############################

    if state == GAME: # check for game state BEFORE loading level
            
        #draw the gound
        pygame.draw.rect(screen, (50, 200, 50), (0, HEIGHT-50,WIDTH,50)) # green

        #draw landing pad
        landing_pad_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 60, 100, 10)
        pygame.draw.rect(screen, (200,200,200), landing_pad_rect)

        #draw trees randomly
        tree_pos = [100, 250, 550, 700]
        for i in tree_pos:
            #the trunk
            pygame.draw.rect(screen, (100,50,0), (i, HEIGHT-80,20,30))
            #draw a fancy polygon for the leaf
            pygame.draw.polygon(screen, (0, 150, 0), [(i -15, HEIGHT -80), (i +35, HEIGHT -80),(i +10, HEIGHT -120)])


        if rocket.alive:
            # gravity always applies
            rocket.vertical_velocity = physics.apply_gravity(rocket.vertical_velocity, dt)

            # thrust when holding SPACE
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                rocket.vertical_velocity = physics.apply_thrust(rocket.vertical_velocity, thrust_power=20, fuel_efficiency=rocket.fuelEfficiency, dt=dt)

            # update position
            rocket.y -= rocket.vertical_velocity


        # ground collision
        ground_y = HEIGHT - 60

        if rocket.y >= ground_y:
            rocket.y = ground_y

            # landing check
            if abs(rocket.vertical_velocity) <= 6: # abs to ensure 100% accuracy
                rocket.vertical_velocity = 0
            else:
                rocket.alive = False # rocket will die in this case, game loss

        # check if the rocket is alive and then draw it, rather than redrawing it over and over
        if rocket.alive:
            rocket_x = WIDTH // 2
            pygame.draw.rect(screen,(200, 50, 50),(rocket_x - 10, rocket.y - 30, 20, 30))

            
        
        
    pygame.display.flip()

    
pygame.quit()
sys.exit()


