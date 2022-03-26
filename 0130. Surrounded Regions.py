"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are
not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped
to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'
"""
from typing import List


def solve(board: List[List[str]]) -> None:
    # use dfs, start from the 'O's on the border
    m, n = len(board), len(board[0])

    def dfs(x, y):
        if not 0 <= x < m or not 0 <= y < n or board[x][y] != 'O':
            return

        board[x][y] = 'A'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    for i in range(m):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][n-1] == 'O':
            dfs(i, n-1)

    for j in range(n):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[m-1][j] == 'O':
            dfs(m-1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'A':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'


