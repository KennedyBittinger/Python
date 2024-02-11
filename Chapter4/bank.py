#!/usr/bin/env python3

"""Module to interact with BankAccount to perform transactions."""

__author__ = 'Kennedy Bittinger'
__date__ = "2/10/24"


import transactions


def get_transaction():
    """Deposit into account.

    Args:
        None

    Returns:
        tran_type (str): type of transaction
        value (float): amount of transaction
    """
    tran_type = input('Type? ')
    print()
    if tran_type != 'x':
        value = float(input('Value? '))
        print()
    else:
        value = 0
    return tran_type, value


def main():
    """Balance bank account.

    Args:
        None

    Returns:
        None
    """
    balance = 0
    tran_type = 'd'
    while tran_type != 'x':
        print('Balance: $' + str(balance))
        tran_type, value = get_transaction()
        if tran_type == 'd':
            balance = transactions.deposit(balance, value)
        elif tran_type == 'w':
            balance = transactions.withdraw(balance, value)
        elif tran_type == 'i':
            balance = transactions.interest(balance, value)


if __name__ == '__main__':
    main()