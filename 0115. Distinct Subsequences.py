"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters
without disturbing the remaining characters' relative positions.
(i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
"""


def numDistinct(s: str, t: str) -> int:
    """
    Use Dynamic Programming
    dp[i][j] - the number of distinct subsequences of s[0:i] which equals t[0:j]
    * if s[i] != t[j], then dp[i][j] = dp[i-1][j]; meaning if last characters are not same, s has to still use the first
    i - 1 to match t's first j
    * if s[i] == t[j], then dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    #
    """
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):  # the "" is a subsequences of any string
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]


# test cases
print(numDistinct("rabbbit", "rabbit"))  # 3
print(numDistinct("babgbag", "bag"))  # 5
print(numDistinct("b", "b"))    # 1
