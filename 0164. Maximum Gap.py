"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Constraints:
    1 <= nums.length <= 105
    0 <= nums[i] <= 109
"""
from typing import List


def maximumGap(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return 0

    # use radix sort
    exp = 1
    buff = [0] * n
    max_val = max(nums)
    while max_val >= exp:
        counter = [0] * 10
        for num in nums:
            digit = ((int)(num / exp)) % 10
            counter[digit] += 1

        for i in range(1, 10):
            counter[i] += counter[i - 1]

        for i in range(n - 1, -1, -1):
            digit = ((int)(nums[i] / exp)) % 10
            buff[counter[digit] - 1] = nums[i]
            counter[digit] -= 1

        nums = buff[::]
        exp *= 10

    # find the max gap
    return max((nums[i + 1] - nums[i]) for i in range(0, n - 1))


# test cases
print(maximumGap([1, 100]))  # 99
