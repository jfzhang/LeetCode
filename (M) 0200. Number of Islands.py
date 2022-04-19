"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.
"""
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])

    def dfs(start_i, start_j):
        if grid[start_i][start_j] == '1':
            grid[start_i][start_j] = '0'
        else:
            return

        if start_i - 1 >= 0:
            dfs(start_i - 1, start_j)
        if start_i + 1 < m:
            dfs(start_i + 1, start_j)
        if start_j - 1 >= 0:
            dfs(start_i, start_j - 1)
        if start_j + 1 < n:
            dfs(start_i, start_j + 1)

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                res += 1
                dfs(i, j)

    return res


# test cases
print(numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))  # 1
