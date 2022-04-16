"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.
"""
from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][1] = nums[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = max(dp[i - 1][0] + nums[i], dp[i - 1][1])

    return max(dp[n - 1])


# test cases
print(rob([1, 2, 3, 1]))  # 4
