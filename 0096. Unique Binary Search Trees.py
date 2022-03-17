"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
    1 <= n <= 19
"""


def numTrees(n: int) -> int:
    # Use Dynamic Programming
    # dp[i] - the number of structurally unique BST's which as i nodes of unique values from 1 to i
    # dp[i] = dp[0]*dp[i-1] + dp[1]*dp[i-2] + ... + dp[i-1]*dp[0]

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = sum(dp[x] * dp[i - x - 1] for x in range(i))

    return dp[n]


# test cases
print(numTrees(3))  # 5
print(numTrees(1))  # 1
