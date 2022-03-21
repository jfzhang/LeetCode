"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
"""
from typing import List


def getRow(rowIndex: int) -> List[int]:
    res = [1]
    if rowIndex == 0:
        return res

    for i in range(0, rowIndex + 1):
        curr = [1]
        for j in range(1, i):
            curr.append(res[j - 1] + res[j])
        curr.append(1)
        res = curr[:]

    return res

