#!/usr/bin/env python3
"""Calculate the number of perfect squares within a number range"""

__author__ = 'Kennedy Bittinger'
__date__ = '2/04/24'

# Prompt the user for the first number
while True:
    try:
        first_number = float(input("First? "))
        print()
        if first_number > 0:
            break
    except ValueError:
        print()

# Prompt the user for the second number
while True:
    try:
        second_number = float(input("Second? "))
        print()
        if second_number > first_number:
            break
    except ValueError:
        print()

# Count variable to keep track of perfect squares
count_perfect_squares = 0

# Check all the numbers between first and second inclusively
for num in range(int(first_number), int(second_number) + 1):
    # Check if any value from 1 to num times itself equals num
    for i in range(1, num + 1):
        if i * i == num:
            print(f"{i} * {i} = {num}")
            count_perfect_squares += 1
            break  # Break the inner loop once a perfect square is found

# Print the count of perfect squares
print(f"Total of {count_perfect_squares} perfect squares")
print()
