#!/usr/bin/env python3

"""Program to calculate the number of frosting tubs needed for a cake."""

__author__ = 'Kennedy Bittinger'
__date__ = '3/17/2024'

import math
import locale as lc
from decimal import Decimal, ROUND_HALF_UP


def get_cake_dimensions():
    """Prompt user for cake dimensions."""
    diameter = Decimal(input('Diameter? '))
    print()
    height = Decimal(input('Height? '))
    print()
    layers = Decimal(input('Layers? '))
    print()
    return diameter, height, layers


def calculate_frosting_tubs(diameter, height, layers):
    """Calculate the number of frosting tubs needed."""
    radius = diameter / Decimal('2')
    area_per_layer = Decimal(str(math.pi)) * radius**2
    area_side = Decimal(str(math.pi)) * diameter * height
    total_area = (area_per_layer * layers) + area_side
    tubs_needed = total_area / Decimal('60')
    return tubs_needed.quantize(Decimal('.01'), ROUND_HALF_UP)


def main():
    """Calculate the number of frosting tubs needed for a cake."""
    try:
        lc.setlocale(lc.LC_ALL, '')
    except lc.Error:
        lc.setlocale(lc.LC_ALL, 'en_US')

    diameter, height, layers = get_cake_dimensions()
    tubs_needed = calculate_frosting_tubs(diameter, height, layers)
    tubs_to_buy = math.ceil(tubs_needed)

    tub_cost = Decimal('1.25')
    total_cost = tubs_to_buy * tub_cost

    print('Num tubs:', str(tubs_to_buy).rjust(5))
    print('Price:', lc.currency(total_cost, grouping=True).rjust(8))


if __name__ == '__main__':
    main()
