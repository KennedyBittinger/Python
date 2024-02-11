#!/usr/bin/env python3

# Prompt the user for base cost of ticket
base_cost = float(input("Base? "))
print()

# Promt the user for additional stops
additional_stops = float(input("Stops? "))
print()

# Total cost
total_cost = base_cost + additional_stops * 25

# Promt the user for discount percentage
discount_percentage = float(input("Discount? "))
print()

# Calculate the discount amount
discount_amount = (discount_percentage / 100) * total_cost

# Cost after discount
cost_after_discount = total_cost - discount_amount

# Cost before discount
print("Cost: $" + str(round(total_cost, 2)))

# Discount
print("Discount: $" + str(round(discount_amount, 2)))

# After discount, final cost
print("Final cost: $" + str(round(cost_after_discount, 2)))
