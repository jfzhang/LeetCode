"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.
"""


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # Use Dynamic Programming
    # dp[i][j] - s1[0:i] and s2[0:j] interleave to form s3[0:i+j]

    l1, l2, l3 = len(s1), len(s2), len(s3)
    if l1 + l2 != l3:
        return False

    dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
    dp[0][0] = True

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i][j - 1]

    return dp[l1][l2]


# test cases
print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
print(isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # False
print(isInterleave("", "", ""))  # True
print(isInterleave("ab", "bc", "babc"))  # True