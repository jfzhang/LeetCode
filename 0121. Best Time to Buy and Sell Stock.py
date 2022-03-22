"""
You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your
profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return
the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = float("inf")
    max_profit = 0

    for x in prices:
        if x < min_price:
            min_price = x
        max_profit = max(max_profit, x - min_price)

    return max_profit