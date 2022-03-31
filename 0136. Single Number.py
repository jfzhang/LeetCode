"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0

    for x in nums:
        res ^= x

    return res
