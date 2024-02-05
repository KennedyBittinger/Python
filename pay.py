#!/usr/bin/env python3
"""Calculate the amount of an employee's paycheck"""

__author__ = 'Kennedy Bittinger'
__date__ = '1/28/24'


def calculate_hourly_pay():
    """Calculate the weekly pay for an hourly employee."""
    # Prompt the user for the hourly pay rate
    hourly_rate = float(input("Hourly pay rate? "))
    print()

    # Ask if the employee is hourly or salaried
    employment_type = input("Hourly/salary? ").lower()
    print()

    # Check if the employee is hourly
    if employment_type == 'h':
        # Prompt the user for the number of hours worked
        hours_worked = float(input("Num hours? "))
        print()

        # Prompt the user to indicate if it was a holiday
        is_holiday = input("Holiday? ").lower()
        print()

        # Calculate the paycheck amount for hourly employees using the function
        if is_holiday == 'y':
            return hourly_rate * hours_worked * 2

        regular_hours = min(40, hours_worked)
        overtime_hours = max(0, hours_worked - 40)
        return hourly_rate * (regular_hours + 1.5 * overtime_hours)

    # Check if the employee is salaried
    if employment_type == 's':
        # For salaried employees, assume a fixed 40 hours
        hours_worked_salaried = 40

        # Calculate the paycheck amount for salaried employees
        return hourly_rate * hours_worked_salaried

    # Handle invalid input for employment type
    return (
        "Invalid employment type. "
        "Please enter 'h' for hourly or 's' for salaried."
    )


# Call the function and display the result
paycheck_amount = calculate_hourly_pay()
print(f"Your weekly pay ${paycheck_amount:.2f}")
