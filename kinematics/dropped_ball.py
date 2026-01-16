"""
Dropped_ Ball _Calculator

Calculates the time it takes for an object to fall from a specific height
assuming zero initial velocity and negligible air resistance.
"""

import math

# Constants
# g: Acceleration due to gravity (m/s^2)
GRAVITY = 9.81

def calculate_fall_time(height_meters: float) -> float:
   
    # Calculates the time to hit the ground from a given height
    
    if height_meters < 0:
        raise ValueError("Height cannot be negative.")

    # Formula: t = sqrt(2h / g)
    time_seconds = math.sqrt((2 * height_meters) / GRAVITY)
    return time_seconds

if __name__ == "__main__":
    # Entry point for the script
    print(" Free Fall Time Calculator ")
    
    try:
        user_input = input("Enter the height of the tower (meters): ")
        height = float(user_input)
        
        fall_time = calculate_fall_time(height)
        
        print(f"Time to impact: {fall_time:.2f} seconds")

    except ValueError as e:
        # To handle both non-numeric inputs and negative heights
        print(f"Input Error: {e}")
