"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0

    res = 0
    low_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > low_price:
            res += prices[i] - low_price
        low_price = prices[i]

    return res