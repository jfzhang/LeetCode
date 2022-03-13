"""
We can scramble a string s to get a string t using the following algorithm:
1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
    * Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y
    where s = x + y.
    * Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become
     s = x + y or s = y + x.
    * Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false

Example 3:
Input: s1 = "a", s2 = "a"
Output: true

Constraints:
    s1.length == s2.length
    1 <= s1.length <= 30
    s1 and s2 consist of lowercase English letters
"""
from collections import Counter
from functools import cache


def isScramble(s1: str, s2: str) -> bool:
    # Use Recursion
    @cache
    def dfs(start1: int, start2: int, length: int) -> bool:
        if s1[start1:start1 + length] == s2[start2:start2 + length]:
            return True

        if Counter(s1[start1:start1 + length]) != Counter(s2[start2:start2 + length]):
            return False

        for i in range(1, length):
            # split without swap
            if dfs(start1, start2, i) and dfs(start1 + i, start2 + i, length - i):
                return True
            # split with swap
            if dfs(start1, start2 + length - i, i) and dfs(start1 + i, start2, length - i):
                return True

        return False

    res = dfs(0, 0, len(s1))
    dfs.cache_clear()
    return res


def isScramble2(s1: str, s2: str) -> bool:
    # Use Dynamic Programming
    # dp[i][j][len] - s1 from i and s2 from j with len are scramble

    n = len(s1)
    dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

    # initialize one character
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = True if s1[i] == s2[j] else False

    # loop length from 2 to n
    for l in range(2, n + 1):
        # loop s1 with length l
        for i in range(n - l + 1):
            # loop s2 with length l
            for j in range(n - l + 1):
                # loop split
                for k in range(1, l):
                    # no swap with splits
                    if dp[i][j][k] and dp[i + k][j + k][l - k]:
                        dp[i][j][l] = True
                        break
                    if dp[i][j + l - k][k] and dp[i + k][j][l - k]:
                        dp[i][j][l] = True
                        break

    return dp[0][0][n]


# test cases
print(isScramble2("great", "rgeat"))  # True
print(isScramble2("abcde", "caebd"))  # False
print(isScramble2("a", "a"))  # True
print(isScramble2("abc", "bca"))  # True
