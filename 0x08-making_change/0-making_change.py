#!/usr/bin/python3
"""find the total number of coins needed to break down an amount"""


def makeChange(coins, total):
    """change money"""
    times = 0
    if total < 1:
        return 0
    coins.sort(reverse=True)
    for elem in coins:
        times += int(total / elem)
        total = total % elem
    if total != 0:
        return -1
    return times
