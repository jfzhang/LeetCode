"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n

    tmp = nums[n - k:] + nums[:n - k]
    for i in range(n):
        nums[i] = tmp[i]


# test cases
a = [1, 2, 3, 4, 5, 6, 7]
rotate(a, 3)
print(a)
