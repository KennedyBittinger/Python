#!/usr/bin/env python3
"""Program to calculate the perimeter of a triangle"""

__author__ = 'Kennedy Bittinger'
__date__ = '1/20/24'

x1 = float(input("Enter x1: "))
print("x1 is " + str(x1))
y1 = float(input("Enter y1: "))
print("y1 is " + str(y1))
x2 = float(input("Enter x2: "))
print("x2 is " + str(x2))
y2 = float(input("Enter y2: "))
print("y1 is " + str(y1))
x3 = float(input("Enter x3: "))
print("x3 is " + str(x3))
y3 = float(input("Enter y3: "))
print("y3 is " + str(y3))

# calculate each side of the triangle
side1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("side1 is " + str(side1))
side2 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
print("side2 is " + str(side2))
side3 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
print("side3 is " + str(side3))

perimeter = round((side1 + side2 + side3), 1)
print("Perimeter is " + str(perimeter))

