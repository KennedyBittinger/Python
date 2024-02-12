#!/usr/bin/env python3

"""Write a program to calculate the total for a fast food order"""

__author__ = 'Kennedy Bittinger'
__date__ = '2/11/24'

# Constants for menu prices
BURGER_PRICE = 1.99
FRIES_PRICE = 0.99
DRINK_PRICE = 1.59
CHICKEN_PRICE = 1.79


def get_item_and_quantity():
    """Prompt the user for the item and a quantity.

    Args:
        None

    Returns:
        item (str): the item selected by the user
        quantity (int): the quantity of the item selected by the user
    """
    item = input("Item? ")
    print()
    quantity = int(input("Qty? "))
    return item, quantity


def calculate_price(item, quantity):
    """Calculate the price for the specified item and quantity.

    Args:
        item (str): the item selected by the user
        quantity (int): the quantity of the item selected by the user

    Returns:
        total_price (float): total price for specified item and quantity
    """
    if item.lower() == "burger":
        total_price = BURGER_PRICE * quantity
    elif item.lower() == "fries":
        total_price = FRIES_PRICE * quantity
    elif item.lower() == "drink":
        total_price = DRINK_PRICE * quantity
    elif item.lower() == "chicken":
        total_price = CHICKEN_PRICE * quantity
    else:
        print("Sorry, we don't have that item on our menu.")
        total_price = 0
    return total_price


def main():
    """Main function to control the flow of the program.

    Args:
        None

    Returns:
        None
    """
    subtotal = 0

    # Loop to enter items
    while True:
        item, quantity = get_item_and_quantity()
        total_price = calculate_price(item, quantity)
        subtotal += total_price

        # Print the subtotal of the order after each entry
        print("\nSubtotal = $" + str(round(subtotal, 2)))

        # Prompt if there are more items to enter
        more = input("More? ")
        if more.lower() != "y":
            break
        print()

    # Order total
    print("\nOrder total: $" + str(round(subtotal, 2)))
    print()


if __name__ == "__main__":
    main()
