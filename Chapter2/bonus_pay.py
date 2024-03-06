#!/usr/bin/env python3

"""Program to calculate bonus pay."""

__author__ = 'Kennedy Bittinger'
__date__ = '3/5/2024'

# Make a 'constant' for amount of bonus per rating
# -- Python does not have a const keyword
# -- Indicate that a variable is constant by using ALL CAPS
BONUS_RATE = 10.75

# print function has end and sep arguments
# -- use end to change from newline to something else
# -- use sep to change the separator from a space
print('Time to calculate your bonus ', end=' -> ')
print(3, 2, 1, sep='...')

# prompt the user for name
# -- input() reads a line from the user and returns a string
# -- print() will print a newline
name = input('Name? ')
print()

# initialize total_ratings to zero
total_ratings = 0

# read, convert, then set total
num_as_string = input('Rating? ')
print()
num_as_int = int(num_as_string)
total_ratings = num_as_int

# do read, convert, add in a single statement using chaining
total_ratings += int(input('Rating? '))
print()
total_ratings += int(input('Rating? '))
print()
total_ratings += int(input('Rating? '))
print()

# do integer division with // (will only get quotient)
avg = total_ratings // 4
print('Your average rating is ' + str(avg))

# round() with the , 2 is rounding to 2 decimal places
bonus_pay = round(avg * BONUS_RATE, 2)

# can use \ for explicit continuation
# -- + is joining/concatenating the strings
# -- \n is an escape sequence for newline
print(name + ' will receive $'
      + str(bonus_pay) + ' bonus'
      + '\nCongratulations!')
