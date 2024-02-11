#!/usr/bin/env python3

"""Write a program to train ticket cost"""

# prompt user for base cost of ticket
base_cost = float(input("Base? "))
print()

# prompt user for the number of additional stops
additional_stops = float(input("Stops? "))
print()

total_cost = base_cost + additional_stops * 25

# prompt user for discount percentage 
discount_percentage = float(input("Discount? "))
print()

# calculate the discount amount
discount_amount = (discount_percentage / 100) * total_cost

# calculate the cost after discount
cost_after_discount = total_cost - discount_amount

# Display the cost before discount, discount, and cost after
print(f"Cost: ${total_cost:.2f}")
print(f"Discount: ${discount_amount:.2f}")
print(f"Final Cost: ${cost_after_discount:.2f}")