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

    """
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
    """

    # use bucket sort
    min_val, max_val = min(nums), max(nums)
    interval = max((max_val - min_val) // (n - 1), 1)
    size = (max_val - min_val) // interval + 1
    bucket = [[-1] * 2 for _ in range(size)]

    for num in nums:
        idx = (num - min_val) // interval
        if bucket[idx][0] == -1:
            bucket[idx][0], bucket[idx][1] = num, num
        else:
            bucket[idx][0] = max(bucket[idx][0], num)
            bucket[idx][1] = min(bucket[idx][1], num)

    # find the max gap
    pre = -1
    ans = 0
    for i in range(size):
        if bucket[i][0] == -1:
            continue
        if pre >= 0:
            ans = max(ans, bucket[i][1] - bucket[pre][0])
        pre = i

    return ans


# test cases
#print(maximumGap([3, 6, 9, 1]))  # 3
print(maximumGap([1, 1000000]))  # 99
