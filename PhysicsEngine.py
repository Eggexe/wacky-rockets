import math

class PhysicsEngine:
    ##################
    # Physics Engine #
    ##################

    """Earth Variables"""
    e_gravityConstant = 9.8
    e_baseAirResistance = 0

    """Rocket Variables"""
    e_rocketSpeed = 0
    e_rocketMass = 0
    e_rocketVelocity = 0

    """Misc Stuff"""
    e_tickRate = 60  # 60 ticks/sec = 60 FPS baseline

    # METHODS
    def get_thrust(self):
        return self.e_rocketSpeed

    def set_gravity(self, gravity):
        self.e_gravityConstant = gravity

    def apply_thrust(self, thrustPower, fuelEfficiency, fuelRemaining):
        # Simplified thrust calculation (can improve later)
        effectiveThrust = thrustPower * fuelEfficiency
        self.e_rocketVelocity += effectiveThrust / self.e_rocketMass
        return self.e_rocketVelocity

    def calculate_fuelEfficiency(self, fuel1_eff, fuel2_eff, oxidiser_eff):
        fuelAVG = (fuel1_eff + fuel2_eff) / 2
        fuelOxidiser = fuelAVG * oxidiser_eff
        final = max(0, min(fuelOxidiser, 1))
        return final
