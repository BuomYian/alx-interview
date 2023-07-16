#!/usr/bin/python3
"""
Module for calculating the fewest number of operations to reach 'n'
"""

import math


def minOperations(n):
    """
    Calculates the fewest number of operations

    Args:
        n (int): The target number of H characters

    returns:
        int: The fewest number of operations needed or 0
    """
    if n <= 1:
        return 0

    factors = []

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    return sum(factors)
