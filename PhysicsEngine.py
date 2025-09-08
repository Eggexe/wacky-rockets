import pygame
import math
#FROM ROCKETCLASS IMPORT ROCKET HERE!!!!

class PhysicsEngine:
    ##################
    # Physics Engine #
    ##################
    # Purpose is to calculate physics stuff for the game
    # and will hold mathematical data the game will need, using realistic numbers


    """Earth Variables"""
    e_gravityConstant = 9.8
    e_baseAirResistance = 0 

    """Rocket Variables"""
    e_rocketSpeed = 0
    e_rocketMass = 0
    e_rocketVelocity = 0
    
    
    """Misc Stuff"""
    e_tickRate = 60 # 60 ticks a second = 60 FPS, baseline

    # METHODS
    def get_thrust():
        return rocketSpeed

    def set_gravity():
        pass # TODO

    def apply_thrust(thrustPower, fuelEfficiency, fuelRemaining):
        pass # TODO

    def calculate_fuelEfficiency(fuel1, fuel2, oxidiser):
        fuelAVG = (fuel1 + fuel2) / 2 # average out scores of 2 fuels
        fuelOxidiser = fuelAVG * oxidiser # multiply fuel efficiency by oxidiser efficiency
        final = max(0, min(fuelOxidiser, 1)) # clamp value between 0 and 1 if bad happen

        # for example
        # fuel1 = kerosene (0.7)
        # fuel2 = liquid hydrogen (0.95)
        # oxidiser = liquid oxygen (0.9)
        # fuel avg = (0.7 + 0.95) ÷ 2 = 0.825
        # fuel * oxidiser = 0.825 × 0.90 = 0.7425
        # clamp/round = 0.74
