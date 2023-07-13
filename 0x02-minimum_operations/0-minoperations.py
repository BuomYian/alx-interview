#!/usr/bin/python3
"""
Module for calculating the fewest number of 
operations to reach 'n' H characters
"""


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

    operations = 0
    paste_buffer = 1  # The initial content in the paste buffer

    while paste_buffer < n:
        if n % paste_buffer == 0:
            paste_buffer = n
        operations += 1
        paste_buffer += paste_buffer

    return operations
