"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0

    for i in range(32):
        total = sum((x >> i) & 1 for x in nums)
        if total % 3:
            if i == 31:
                res -= (1 << i)
            else:
                res |= (1 << i)

    return res
