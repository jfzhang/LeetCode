"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again)
"""
from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    if not prices or k == 0:
        return 0

    n = len(prices)
    k = min(k, n // 2)  # the max transaction would be less than n//2, the transaction in same day not add profit
    buy = [[0] * (k + 1) for _ in range(n)]  # buy[i][j] - max profit in day [0,i] with j transaction and hold stock
    sell = [[0] * (k + 1) for _ in range(n)]  # sell[i][j] - max profit in day [0,i] with j transaction and no stock

    buy[0][0], sell[0][0] = -prices[0], 0
    for j in range(1, k + 1):
        buy[0][j] = sell[0][j] = float("-inf")

    for i in range(1, n):
        buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
        for j in range(1, k + 1):
            buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
            sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])

    return max(sell[n - 1])


# test cases
print(maxProfit(2, [1, 2, 4]))  # 3
print(maxProfit(4, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))  # 15