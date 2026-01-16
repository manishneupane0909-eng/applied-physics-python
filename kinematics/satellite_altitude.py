"""
Satellite Altitude Calculator
-----------------------------
Calculates the altitude of a satellite orbiting Earth based on its period.
Derivation based on Kepler's Third Law and Newton's Law of Gravitation.

Author: Manish Neupane

"""

import math

# Constants
# G: Gravitational constant (m^3 kg^-1 s^-2)
# M: Mass of Earth (kg)
# R: Radius of Earth (m)
G = 6.67e-11
M = 5.97e24
R = 6371 * 1000 

def calculate_altitude(period_seconds: float) -> float:
    """
    Formula:
        h = ( (G * M * T^2) / (4 * pi^2) )^(1/3) - R
    """
    numerator = G * M * (period_seconds ** 2)
    denominator = 4 * (math.pi ** 2)
    
    # Calculate orbital radius (r) from center of Earth
    orbital_radius = (numerator / denominator) ** (1/3)
    
    # Altitude is orbital radius minus Earth's radius
    altitude = orbital_radius - R
    
    return altitude

if __name__ == "__main__":
    try:
        user_period = float(input("Enter the orbital period T (seconds): "))
        altitude = calculate_altitude(user_period)
        
        print(f"Calculated Altitude: {altitude:.2f} meters")
        print(f"({altitude/1000:.2f} km)")
        
    except ValueError:
        print("Error: Please enter a valid numeric value for the period.")
