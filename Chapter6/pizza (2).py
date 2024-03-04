#!/usr/bin/env python3

"""Module to order a pizza."""

__author__ = 'Kennedy Bittinger'
__date__ = '6/12/2020'

import random


def remove_topping(tops, to_remove):
    """Remove a topping from the list.

    Args:
        tops (list): list of toppings
        to_remove (str): topping to remove

    Returns:
        None
    """
    if to_remove.lower() in tops:
        # Must know that item is in tops before calling remove
        tops.remove(to_remove.lower())
        to_remove = to_remove.upper()
        print('Removed: ' + to_remove)
    else:
        print('Sorry that topping is not in the list')


def organize_toppings(tops):
    """Organize toppings in the list.

    Args:
        tops (list): list of toppings
        to_remove (str): topping to remove

    Returns:
        None
    """
    organize = input('s(h)uffle, (r)everse, (s)ort, (n)one? ')
    if organize.upper() == 'H':
        random.shuffle(tops)
    elif organize.upper() == 'R':
        tops.reverse()
    elif organize.upper() == 'S':
        # sort values as lowercase, but keep original case in the list
        tops.sort(key=str.lower)


def order_toppings(tops, order):
    """Add toppings to order based on user choices.

    Args:
        tops (list): list of toppings
        order (list): list of lists of toppings and count

    Returns:
        None
    """
    # Create a list of lists, each row is a topping with 0 count
    for top in tops:
        one_topping = []
        one_topping.append(top)
        one_topping.append(0)
        order.append(one_topping)

    # Prompt user, adding 1 to count of matching topping
    topping = input(str(tops) + '? ')
    print()
    while topping != 'exit':
        # Must know that item is in tops before calling index
        order[tops.index(topping)][1] += 1
        topping = input(str(tops) + '? ')
        print()
    order.sort()    # sorts by first item in each list
    print(order)


def main():
    """Add toppings to order based on user choices.

    Args:
        None

    Returns:
        None
    """
    # lists are [ ] and are mutable
    toppings = ['extra cheese', 'pepperoni', 'mushrooms']
    topping = 'not exit'

    while topping != 'exit':
        topping = input('Topping? ')
        print()
        toppings.append(topping.lower())
    toppings.pop()
    print(toppings)

    topping = input('Topping to remove from menu? ')
    print()
    remove_topping(toppings, topping)
    print(toppings)

    organize_toppings(toppings)
    print(toppings)

    order = []
    order_toppings(toppings, order)

    # tuples are ( ) and are immutable
    sizes = ('small', 'medium', 'large', 'extra-large')
    size = input(('Choose a size: ' + str(sizes)) + '? ')
    print('You ordered a '
          + size
          + ' pizza with '
          + str(order))

    # capitalize and print order toppings with enumerate
    for ind, topping in enumerate(order):
        order[ind][0] = topping[0].upper()
    for num, topping in enumerate(order, start=1):
        print('Topping', num, 'is', topping[1], topping[0])


if __name__ == '__main__':
    main()
