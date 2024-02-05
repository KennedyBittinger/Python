#!/usr/bin/env python3

"""Write a program to calculate the price of a movie ticket"""

__author__ = 'Kennedy Bittinger'
__date__ = '1/27/24'

# Prompt the user for time of day, weekend, and age
time_of_day = input("morning, noon, or night? ")
print()
weekend = input("weekend (y/n)? ")
print()
age = int(input("age? "))  # Convert age to an integer
print()

# Determine the price based on the time of day
if time_of_day == "morning":
    price = 10
elif time_of_day == "noon":
    price = 12
elif time_of_day == "night":
    price = 14
else:
    print("Invalid time of day")

# Apply surcharge for the weekend
if weekend.lower() == 'yes' or weekend.lower() == 'y':
    weekend_surcharge = 2.50
else:
    weekend_surcharge = 0

# Apply discount for kids and seniors
if age <= 12 or age >= 65:
    discount = 0.10
else:
    discount = 0

# Calculate the final price
final_price = price + weekend_surcharge - (price * discount)

# Display the final price of the ticket
print()
print(f"Your ticket costs ${final_price:.1f}")
