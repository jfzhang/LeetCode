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
    wordSet = set(wordList)  # use Set to easily find the words

    if endWord not in wordSet:  # edge case
        return []

    word_len = len(beginWord)
    q = set()  # used to store the node in each layer when building a tree
    q.add(beginWord)
    next_map = {}  # a str->Set() hashmap used to store the mapping from one word to others
    found = False
    level = 0

    while q:
        # for save level, there might have multiple solution, so need to loop all elements in this level
        temp_q = q.copy()
        q.clear()
        level += 1

        # remove the visited words, so that the next level would not repeat it to trim the tree
        for curr_word in temp_q:
            if curr_word in wordSet:
                wordSet.remove(curr_word)

        for curr_word in temp_q:
            if curr_word not in next_map:
                next_map[curr_word] = set()

            # loop the possible transform
            for i in range(0, word_len):
                for j in range(26):
                    if j == ord(curr_word[i]) - ord('a'):
                        continue
                    next_word = curr_word[0:i] + chr((ord('a') + j)) + curr_word[i + 1:]
                    if next_word not in wordSet:
                        continue
                    # find a new node
                    next_map[curr_word].add(next_word)
                    q.add(next_word)

                    if not found and next_word == endWord:
                        found = True
        if found:  # if found, don't need to continue building the tree
            break

    res = []

    # a dfs traversal function to help get the final result
    def getPath(begin, end, path, seq):
        # add a path when arriving right level and find the end word
        if seq == 0:
            if begin == end:
                res.append(path[::])
            return

        for x in next_map[begin]:
            getPath(x, end, path + [x], seq - 1)

    if found:
        getPath(beginWord, endWord, [beginWord], level)

    return res


# test cases
print(findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]

print(findLadders("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
# [['red', 'ted', 'tex', 'tax'], ['red', 'ted', 'tad', 'tax'], ['red', 'rex', 'tex', 'tax']]

print(findLadders("ta", "if", ["ts", "sc", "ph", "ca", "jr", "hf", "to", "if", "ha", "is", "io", "cf", "ta"]))
# [['ta', 'ha', 'hf', 'if'], ['ta', 'to', 'io', 'if'], ['ta', 'ts', 'is', 'if'], ['ta', 'ca', 'cf', 'if']]
