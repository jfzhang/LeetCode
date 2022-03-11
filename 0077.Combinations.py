"""
Given two integers n and k, return all possible combinations of k numbers out of the range[1, n].

You may return the answer in any order.

Example 1: Input: n = 4, k = 2
Output:
[
    [2, 4],
    [3, 4],
    [2, 3],
    [1, 2],
    [1, 3],
    [1, 4],
]

Example 2: Input: n = 1, k = 1
Output: [[1]]

Constraints: 1 <= n <= 20, 1 <= k <= n
"""
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    # backtrack
    def backtrack(start: int, comb: List[int], left: int):
        if left == 0:
            result.append(comb)
            return

        # for i in range(start, n + 1):
        for i in range(start, n + 1 - (left - 1)):  # optimize by trimming, need enough left for k combination
            backtrack(i + 1, comb + [i], left - 1)

    result = []
    backtrack(1, [], k)

    return result


# test cases
print(combine(4, 2))
print(combine(1, 1))
