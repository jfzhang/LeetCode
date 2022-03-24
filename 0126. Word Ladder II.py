"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences
from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of
the words [beginWord, s1, s2, ..., sk].

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
    1 <= beginWord.length <= 5
    endWord.length == beginWord.length
    1 <= wordList.length <= 1000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
"""
from collections import defaultdict
from typing import List


def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    # use BFS
    wordSet = set(wordList)  # use Set to easily find the words
    word_len = len(beginWord)
    q = set()
    q.add(beginWord)
    next_to_pre = {}
    found = False
    level = 0

    if endWord not in wordSet:
        return []

    while q:
        temp_q = q.copy()
        q.clear()
        level += 1
        for curr_word in temp_q:
            # if the next_word in the WordSet and used,
            # it could be removed from it, because reusing it has longer path
            if curr_word in wordSet:
                wordSet.remove(curr_word)

            for i in range(0, word_len):
                for j in range(26):
                    if j == ord(curr_word[i]) - ord('a'):
                        continue
                    next_word = curr_word[0:i] + chr((ord('a') + j)) + curr_word[i + 1:]
                    if next_word not in wordSet:
                        continue
                    if next_word not in next_to_pre:
                        next_to_pre[next_word] = set()
                    next_to_pre[next_word].add(curr_word)
                    q.add(next_word)

                    if not found and next_word == endWord:
                        found = True

        if found:
            break

    res = []

    def getPath(begin, end, path, level):
        if level == 0:
            if begin == end:
                res.append(path[::-1])
            return

        for x in next_to_pre[end]:
            getPath(begin, x, path + [x], level-1)

    if found:
        getPath(beginWord, endWord, [endWord], level)

    return res


# test cases
#print(findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
#print(findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
print(findLadders("ta", "if", ["ts","sc","ph","ca","jr","hf","to","if","ha","is","io","cf","ta"]))
