import os

class RocketClass:
    # what are the table thingies for?
    # FUEL_NAME, FUEL_EFFICIENCY_VAL, FUEL_ATOM_ECONOMY
    # FUEL_NAME is the name of the fuel/oxidiser
    # FUEL_EFFICIENCY_VAL is how efficient the fuel is
    # FUEL_ATOM_ECONOMY is another measure of efficiency for reactions
    # reactions ARENT CODED, its another value to avoid players picking best options
    # balancing basically^^^
   
   
   # changed from 2d list to dic, talk abt
    r_Fuels = {
        "Kerosene": (0.75, 0.7),
        "RP-1": (0.8, 0.75),
        "Liquid Hydrogen": (0.95, 0.95),
        "Methane": (0.9, 0.9),
        "Ethanol": (.7, 0.85),
        "Solid Fuel": (0.5, 0.35),
        "Hydrazine": (0.65, 0.5),
        "Ammonia": (0.5, 0.45),
        "NTPF": (1.00, 0.8)
        }

    r_Oxidiser = {
        "Liquid Oxygen": (0.9, 0.85),
        "Nitrous Oxide": (0.6, 0.65).,
        "Nitrogen Tetroxide": (0.75, 0.7),
        "Flourine": (1.0, 0.3)
        }

    def __init__(self, fuel1, fuel2, oxidiser1):
        imagePath = ""
        # TAKEN FROM PHYSICSENGINE, remember for the fuel stuff
        # for example
        # fuel1 = kerosene (0.7)
        # fuel2 = liquid hydrogen (0.95)
        # oxidiser = liquid oxygen (0.9)
        # fuel avg = (0.7 + 0.95) ÷ 2 = 0.825
        # fuel * oxidiser = 0.825 × 0.90 = 0.7425
        # clamp/round = 0.74
