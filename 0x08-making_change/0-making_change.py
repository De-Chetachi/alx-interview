#!/usr/bin/python3
"""make change"""


def makeChange(coins, money):
    """
    make change function"""
    if money < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if money == 0:
            break
        num = money // coin
        money -= num * coin
        count += num
    return count if money == 0 else -1
