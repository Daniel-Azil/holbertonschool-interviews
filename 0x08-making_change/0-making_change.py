#!/usr/bin/python3
"""
    A module that counts given coins.
"""


def makeChange(coins, total):
    """
        A class that calculates the minimum number of coins required to achieve
        a specific total using a collection of coins with various values.
    """
    if total <= 0:
        return 0
    remainder = total
    coin_count = 0
    index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remainder > 0:
        if index >= num_coins:
            return -1
        if remainder - sorted_coins[index] >= 0:
            remainder -= sorted_coins[index]
            coin_count += 1
        else:
            index += 1
    return coin_count
