# Problem 2.1: Dropped Ball
import math

g = 9.81
h = float(input("Enter the height of the tower (meters): "))
t = math.sqrt((2 * h) / g)

print(f"Time to hit the ground is {t:.2f} seconds")