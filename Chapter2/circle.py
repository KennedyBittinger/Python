#!/usr/bin/env python3
"""Program to calculate the area and circumference of a circle"""

__author__ = 'Kennedy Bittinger'
__date__ = "1/21/24"

# Prompt the user for a radius
radius = float(input("Radius: "))
print()

# Make a constant PI for π. Set its value to 3.14
PI = 3.14

# Calculate the area using πr^2, and round by 3
area = PI * radius ** 2
print("Area:", round(area, 3))

# Calculate the circumference using 2πr, and round by 3
circumference = 2 * PI * radius
print("Circumference:", round(circumference, 3))
