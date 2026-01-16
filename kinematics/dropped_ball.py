# A ball is again dropped from a tower of height h with initial velocity zero. 
# Write a program that asks the user to enter the height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground, ignoring air resistance. 
# Use your program to calculate the time for a ball dropped from a 100 m high tower
import math

g = 9.81
h = float(input("Enter the height of the tower (meters): "))
t = math.sqrt((2 * h) / g)

print(f"Time to hit the ground is {t:.2f} seconds")
