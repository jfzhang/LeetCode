"""
Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum
of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = [[1]]

    for i in range(1, numRows):
        pre = res[i - 1]
        curr = [1]
        for j in range(1, i):
            curr.append(pre[j - 1] + pre[j])
        curr.append(1)
        res.append(curr)

    return res


# test cases
print(generate(5))
