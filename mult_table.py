#!/usr/bin/env python3

"""Write a program to print a multiplication table"""

__author__ = 'Kennedy Bittinger'
__date__ = '2/3/24'


start = -1
while start < 1 or start > 10:
    start = int(input('Start? '))
    print()

stop = -1
while stop < 1 or stop > 10:
    stop = int(input('Stop? '))
    print()

print('*', end='	')
for i in range(start, stop + 1):
    print('(' + str(i) + ')', end='	')
print()

for i in range(start, stop + 1):
    print('(' + str(i) + ')', end='	')
    for j in range(start, stop + 1):
        print(i * j, end='	')
    print()
    