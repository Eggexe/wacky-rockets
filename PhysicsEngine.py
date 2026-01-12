import math

class PhysicsEngine:
    """Earth variables"""
    e_gravityConstant = 9.8
    e_baseAirResistance = 0

    """rocket variables"""
    e_rocketSpeed = 0
    e_rocketMass = 0
    e_rocketVelocity = 0

    e_tickrate = 60 # 60 fps baseline


    # METHODS

    def get_thrust(self):
        return self.e_rocketSpeed

    def set_gravity(self, gravity):
        self.e_gravityConstant = gravity

    def apply_thrust(self,thrustPower, fuelEfficiency, fuelRemaining):
        effectiveThrust = thrustPower * fuelEfficiency
        self.e_rocketVelocity += effectiveThrust / self.e_rocketMass
        return self.e_rocketVelocity

    def calculate_fuelEfficiency(self, fuel1_eff, oxidiser_eff):
        fuelMix = fuel1_eff * oxidiser_eff
        final = math.clamp(fuelMix, 0, 1)
        return final

    
