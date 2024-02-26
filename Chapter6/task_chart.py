#!/usr/bin/env python3

"""Task Chart Management Program."""

__author__ = 'Kennedy Bittinger'
__date__ = '2/21/24'


NUM_PEOPLE = 5
NUM_TASKS = 8


def draw_chart(chart):
    """Draw the task chart.

    Args:
        chart (list): two-dimensional list, person with 8 tasks per row

    Returns:
        None
    """
    for person in chart:
        for task in person:
            print(task, end='   ')
        print()


def main():
    """Manage task chart.

    Args:
        None

    Returns:
        None
    """
    people = ('Jane', 'Paul', 'Kate', 'John', 'Dave')

    chart = []
    for i in range(NUM_PEOPLE):
        person = [people[i]]
        person += ['_'] * NUM_TASKS
        chart.append(person)
    draw_chart(chart)

    person = input('Person? ')
    print()
    while person in people:
        task = int(input('Task? '))
        print()
        chart[people.index(person)][task] = 'X'
        draw_chart(chart)
        person = input('Person? ')
        print()


if __name__ == '__main__':
    main()
