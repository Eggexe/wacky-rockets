import os
from PhysicsEngine import PhysicsEngine

class RocketClass:
    # what are tables for?
    # FUEL_NAME, FUEL_EFFIENCY
    # fuel name is a label of fuel to distinguish it apart
    # fuel efficiency is how efficient the fuel is, * together with
    # oxidiser to create a mixture and affects thrust


    r_Fuels = {
        "Kerosene": 0.75,
        "RP-1": 0.8,
        "Liquid Hydrogen": 0.95,
        "Methane": 0.9,
        "Ethanol": 0.65,
        "Solid Fuel": 0.45,
        "Hydrazine": 0.7,
        "Ammonia": 0.2,
        "NTPF": 1.0
        }

    r_Oxidiser = {
        "liquid Oxygen": 0.9,
        "Nitrous Oxide": 0.6,
        "Nitrogen Tetroxide": 0.75,
        "Flourine": 1.0
        }

    def __init__(self, fuel1, oxidiser1):
        imagePath = "" # path to display rocket texture

        # instantiate initialised vars + physics engine
        self.fuel1 = fuel1
        self.oxidiser1 = oxidiser1
        self.physics = PhysicsEngine()

        # rip the fuel and oxidiser values from tables above
        f1_eff = self.r_Fuels[fuel1]
        ox_eff = self.r_Oxidiser[oxidiser1]

        # send values to physics engine
        self.fuelEfficiency = self.physics.calculate_fuelEfficiency(f1_eff, ox_eff)

        # rocket stats
        self.mass = 1000
        self.velocity = 0
        
