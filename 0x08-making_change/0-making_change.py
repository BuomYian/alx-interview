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

    coins.sort(reverse=True)  # Sort coins in descending order

    coin_count = 0
    remaining_total = total

    for coin in coins:
        if remaining_total >= coin:
            num_coins = remaining_total // coin
            coin_count += num_coins
            remaining_total -= num_coins * coin

    if remaining_total == 0:
        return coin_count
    else:
        return -1
