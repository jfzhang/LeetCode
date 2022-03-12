"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
    rows == matrix.length
    cols == matrix[i].length
    1 <= row, cols <= 200
    matrix[i][j] is '0' or '1'
"""
from typing import List


def maximalRectangle(matrix: List[List[str]]) -> int:
    # for each row, leverage the 0084 Largest Rectangle in Histogram
    # just need to calculate the heights
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

    m, n = len(matrix), len(matrix[0])
    res = 0
    height = [0] * n
    for i in range(m):
        for j in range(n):
            height[j] = 0 if matrix[i][j] == "0" else height[j] + 1
        res = max(res, largestRectangleArea(height))

    return res


# test cases
print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # 6
print(maximalRectangle([["0","1"],["1","0"]]))  # 1
