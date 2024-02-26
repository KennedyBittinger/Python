#!/usr/bin/env python3

"""program to read positive numbers and print the data sorted in many ways"""

__author__ = 'Kennedy Bittinger'
__date__ = '2/26/24'


def main():
    """Read positive numbers and print the data sorted in various ways.

    Args:
        None

    Returns:
        None
    """
    numbers = []

    # Prompt the user for positive integers
    while True:
        num_str = input("Num? ")
        if num_str == '-1':
            break
        try:
            num = int(num_str)
            if num <= 0:
                print("Please enter a positive integer.")
            else:
                numbers.append(num)
                print()
        except ValueError:
            print("Invalid input.")

    if numbers:
        # Printing all numbers in the order they were entered
        print("\nAll (sorted):", sorted(numbers, reverse=True))

        # Printing all even numbers, maintaining order
        evens = [num for num in numbers if num % 2 == 0]
        print("Evens:", evens)

        # Printing all odd numbers, maintaining order
        odds = [num for num in numbers if num % 2 != 0]
        print("Odds:", odds)
    else:
        print("No data entered.")

    print()


if __name__ == "__main__":
    main()
