"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""
from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    # Use Bit Manipulation
    nums.sort()

    res = []
    n = len(nums)
    for i in range(2 ** n):
        comb = []
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                if j > 0 and not (i >> (j - 1)) & 1 and nums[j] == nums[j - 1]:
                    flag = False
                    break
                comb += [nums[j]]
        res.append(comb) if flag else []

    return res


print(subsetsWithDup([1, 2, 2, 2]))