"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
"""
import functools
from typing import List


def largestNumber(nums: List[int]) -> str:
    nums_str = map(str, nums)

    def cmp(a, b):
        if a + b == b + a:
            return 0
        elif a + b > b + a:
            return 1
        else:
            return -1

    nums_str = sorted(nums_str, key=functools.cmp_to_key(cmp), reverse=True)
    return ''.join(nums_str) if nums_str[0] != '0' else '0'
