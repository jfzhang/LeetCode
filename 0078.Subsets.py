"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* All the numbers of nums are unique.
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    for i in range(2 ** n):
        comb = []
        for j in range(n):
            comb += [nums[j]] if (i >> j) & 1 else []
        res.append(comb)

    return res


print(subsets([1,2,3]))
