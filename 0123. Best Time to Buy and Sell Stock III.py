"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 105
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Dynamic Program
    There's 5 status in a particular day S1) no buy, no sell; S2) buy once, no sell; S3) buy once, sell once;
    S4) buy twice, sell once; S5) buy twice and sell twice
    For S1, it would not generate any profits, so we don't need to consider it
    For S2, if day (i) is S2, then S2 = max( S2 (i-1), -price[i] ), meaning no operator or buy once in day i
    For S3, if day (i) is S3, then S3 = max( S3 (i-1), S2 (i-1) + price[i]), meaning no operator or sell once if only
    buy onece
    For S4, if day (i) is S4, then S4 = max( S4 (i-1), S3 (i-1) - price[i])
    For S5, if day (i) is S5, then S5 = max( S5 (i-1), S4 (i-1) + price[i])
    """
    # initialize
    s2, s3, s4, s5 = -prices[0], 0, -prices[0], 0

    for i in range(1, len(prices)):
        s2 = max(s2, -prices[i])
        s3 = max(s3, s2 + prices[i])
        s4 = max(s4, s3 - prices[i])
        s5 = max(s5, s4 + prices[i])

    return s5


# test cases
# print(maxProfit([3,3,5,0,0,3,1,4]))    # 6
print(maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))  # 13
