#!/usr/bin/env python3

"""Define a BankAccount class"""

__author__ = 'Kennedy Bittinger'
__date__ = "2/10/24"


def deposit(balance, amount):
    """Deposit into account.

    Args:
        balance (float): current balance
        amount (float): how much to deposit

    Returns:
        balance (float): updated balance
    """
    return balance + amount


def withdraw(balance, amount):
    """Withdraw from account.

    Args:
        balance (float): current balance
        amount (float): how much to withdraw

    Returns:
        balance (float): updated balance
    """
    return balance - amount


def interest(balance, rate):
    """Apply interest to balance.

    Args:
        balance (float): current balance
        rate (float): interest rate as a percent

    Returns:
        balance (float): updated balance
    """
    return round(balance * (1 + rate / 100.0), 2)