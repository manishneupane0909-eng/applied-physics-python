import math

G = 6.67e-11
M = 5.97e24
R = 6371e3

T = float(input("Enter orbital period T (seconds): "))

r = ((G * M * T**2) / (4 * math.pi**2)) ** (1/3)
h = r - R

print(f"Altitude: {h:.3e} meters")
