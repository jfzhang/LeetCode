"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

 Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    # Use Backtracking

    def search_board(start_i: int, start_j: int, word: str):
        if not word:
            return True

        visited[start_i][start_j] = 1
        for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_i, next_j = start_i + direction[0], start_j + direction[1]
            if 0 <= next_i < m and 0 <= next_j < n and not visited[next_i][next_j] and board[next_i][next_j] == word[0]:
                if search_board(next_i, next_j, word[1:]):
                    return True
        visited[start_i][start_j] = 0
        return False

    m = len(board)
    n = len(board[0])
    visited = [[0] * n for _ in range(m)]

    # find the first character
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if search_board(i, j, word[1:]):
                    return True
    return False


# test cases
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))    # True
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))   # False