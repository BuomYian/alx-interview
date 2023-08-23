#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number
    # of coins needed for each amount from 1 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Zero coins needed to make change for 0

    # Iterate through each coin value
    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(
                min_coins[amount], min_coins[amount - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1  # Total cannot be met by any combination of coins

    return min_coins[total]
