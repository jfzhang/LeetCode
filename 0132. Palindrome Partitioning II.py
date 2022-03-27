"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase English letters only
"""


def minCut(s: str) -> int:
    # First, use dynamic Programming to get all the partitions which are palindrome
    n = len(s)
    dp = [[True] * n for _ in range(n)]  # dp[i:j] is True if it is a palindrome
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

    # Then, use dynamic programming again to find the minimum cuts
    # f[i] the minimum cuts for s[:i+1], so f[i] = min(f[j]) + 1 where 0<=j<i and s[j+1,i] is a palindrome
    f = [n + 1] * n
    for i in range(n):
        if dp[0][i]:
            f[i] = 0
        else:
            for j in range(i):
                if dp[j + 1][i]:
                    f[i] = min(f[i], f[j] + 1)

    return f[n - 1]


# test cases
print(minCut("aab"))  # 1
print(minCut("a"))  # 0
print(minCut("ab"))  # 1
