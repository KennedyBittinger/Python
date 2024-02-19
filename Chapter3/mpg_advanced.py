#!/usr/bin/env python3

"""The miles per gallon program."""


__author__ = 'Kennedy Bittinger'
__date__ = '2/13/24'

# Display a title
print("The Miles Per Gallon program")
print()

# Get input from the user
miles_driven = float(input("Enter miles driven:         "))
gallons_used = float(input("Enter gallons of gas used:  "))

if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
else:
    # Calculate and display miles per gallon
    mpg = round((miles_driven / gallons_used), 2)
    print("Miles Per Gallon:          ", mpg)

    print()
    print("Bye!")