from PhysicsEngine import PhysicsEngine

class Rocket:
    r_Fuels = {
        "Kerosene": (0.75, 0.7),
        "RP-1": (0.8, 0.75),
        "Liquid Hydrogen": (0.95, 0.95),
        "Methane": (0.9, 0.9),
        "Ethanol": (0.7, 0.85),
        "Solid Fuel": (0.5, 0.35),
        "Hydrazine": (0.65, 0.5),
        "Ammonia": (0.5, 0.45),
        "NTPF": (1.00, 0.8)
    }

    r_Oxidiser = {
        "Liquid Oxygen": (0.9, 0.85),
        "Nitrous Oxide": (0.6, 0.65),
        "Nitrogen Tetroxide": (0.75, 0.7),
        "Fluorine": (1.0, 0.3)
    }

    def __init__(self, fuel1, fuel2, oxidiser1):
        self.fuel1 = fuel1
        self.fuel2 = fuel2
        self.oxidiser1 = oxidiser1
        self.physics = PhysicsEngine()

        # Pull efficiency values from the dicts
        f1_eff, _ = self.r_Fuels[fuel1]
        f2_eff, _ = self.r_Fuels[fuel2]
        ox_eff, _ = self.r_Oxidiser[oxidiser1]

        # Calculate efficiency
        self.fuelEfficiency = self.physics.calculate_fuelEfficiency(f1_eff, f2_eff, ox_eff)

        # Rocket stats
        self.mass = 1000
        self.velocity = 0
