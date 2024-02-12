#!/usr/bin/env python3

"""Write a program to calculate the total cost of a meal at a restaurant."""

__author__ = 'Kennedy Bittinger'
__date__ = '2/11/24'

# Provide a welcome message
print("Welcome to the restaurant cost calculator!\n")

# Prompt the user for the base cost of the meal
base_cost = float(input("Please enter the base cost of the meal: "))
    
# Prompt the user for the number of drinks ordered
drinks_ordered = int(input("How many drinks did you order? "))

# Prompt the user for the number of appetizers ordered
appetizers_ordered = int(input("How many appetizers did you order? "))

# Prompt the user for the number of main courses ordered
main_courses_ordered = int(input("How many main courses did you order? "))

# Prompt the user for the tax rate
tax_rate = float(input("What is the tax rate (in percentage)? "))

# Calculate total cost without tax
subtotal = base_cost + drinks_ordered * 2 + appetizers_ordered * 6 + main_courses_ordered * 10

 # Calculate tax amount
tax_amount = subtotal * (tax_rate / 100)

# Calculate total cost including tax
total_cost = subtotal + tax_amount
print()

# Output the subtotal (total cost before tax), tax amount, and total cost after tax
print("\nSubtotal: $" + str(round(subtotal, 2)))
print("Tax: $" + str(round(tax_amount, 2)))
print("Total: $" + str(round(total_cost, 2)))
