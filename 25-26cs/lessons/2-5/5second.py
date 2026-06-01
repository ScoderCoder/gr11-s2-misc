#!/usr/bin/python

# 10/02/2026
# Sougato

import math 

# Receive Coordinates
x1 = float(input("Enter coordinate 1 x-position: "))
y1 = float(input("Enter coordinate 1 y-position: "))
x2 = float(input("Enter coordinate 2 x-position: "))
y2 = float(input("Enter coordinate 2 y-position: "))

# Formula for distance between 2 points
d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

# Print and round
print(f"\nDistance between the ({x1}, {y1}) & ({x2}, {y2}): {round(d, 2)}")


