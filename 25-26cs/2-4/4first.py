#!/usr/bin/python

# 09/02/2026
# Sougato

import math 

radius = float(input("Enter the radius of circle: "))

circumference = 2*math.pi*radius
area = math.pi*radius**2

print(f"\nA circle with radius {radius} has a circumference of {circumference} cm an an area of {area} cm^2.")
