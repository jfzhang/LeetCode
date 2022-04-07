"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and
return the product.
"""
from typing import List


def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]

    max_dp = [float("-inf")] * n
    min_dp = [float("inf")] * n

    max_dp[0], min_dp[0] = nums[0], nums[0]

    for i in range(1, n):
        max_dp[i] = max(max_dp[i - 1] * nums[i], nums[i], min_dp[i - 1] * nums[i])
        min_dp[i] = min(max_dp[i - 1] * nums[i], nums[i], min_dp[i - 1] * nums[i])

    return max(max_dp[i] for i in range(n))
