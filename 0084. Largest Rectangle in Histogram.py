"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return
the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
    1 <= heights.length <= 105
    0 <= heights[i] <= 104
"""
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    # Use Monotonic Stack
    stack = []
    n = len(heights)
    left, right = [0] * n, [n] * n

    # get the left and right for each bar
    for i in range(len(heights)):
        # if the stacked bar is bigger than the current bar, pop it and the current pos is its right
        while stack and heights[i] < heights[stack[-1]]:
            right[stack.pop()] = i

        # now all the stacked bars are smaller than the current bar, the left of current bar the top in stack
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    return max((right[i] - left[i] - 1) * heights[i] for i in range(n))


# test cases
print(largestRectangleArea([2,1,5,6,2,3]))  # 10
print(largestRectangleArea([2,4]))  # 4
print(largestRectangleArea([0,9]))  # 9


