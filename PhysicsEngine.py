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


    # GENERIC METHODS

    def get_thrust(self):
        return self.e_rocketSpeed

    def set_gravity(self, gravity):
        self.e_gravityConstant = gravity

    def calculate_fuelEfficiency(self, fuel1_eff, oxidiser_eff):
        fuelMix = fuel1_eff * oxidiser_eff
        final = max(0, min(fuelMix,1))
        return final


    # ROCKET MOVING METHODS
    def apply_gravity(self, velocity, dt):
        #gravity always should pull down
        #dt = delta time, personal note
        velocity -= self.e_gravityConstant * dt
        return velocity

    def apply_thrust(self, velocity, thrust_power, fuel_efficiency, dt):
        #thrust makes rocket go up
        thrust = thrust_power * fuel_efficiency
        velocity += thrust * dt
        return velocity

    
