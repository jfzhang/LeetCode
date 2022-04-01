"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
 of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)

    dp = [False] * (len(s) + 1)  # dp[i] is True if s[0:i] can be break into word
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


# test case
print(wordBreak("leetcode", ["leet", "code"]))
