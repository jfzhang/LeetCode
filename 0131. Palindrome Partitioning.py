"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible
palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters
"""
from typing import List


def partition(s: str) -> List[List[str]]:
    # firstly, use Dynamic Program to find all the partitions which are palindrome
    # use dfs to find all partitions

    n = len(s)
    dp = [[True] * n for _ in range(n)]  # dp[i][j] represents s[i:j] is a palindrome

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

    res = []

    def dfs(start, path):
        if start == n:
            res.append(path)
            return

        for pos in range(start, n):
            if dp[start][pos]:
                dfs(pos + 1, path + [s[start:pos + 1]])

    dfs(0, [])
    return res


# test cases
print(partition("aab"))  # [["a","a","b"],["aa","b"]]
print(partition("a"))   # [["a"]]
