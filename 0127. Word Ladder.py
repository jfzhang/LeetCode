"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""
from typing import List


# Comparing to 127, it's only asking to find the steps, instead of each path
# So, to be simple, we don't need to maintain the word transform mapping from one to another
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # use bi-direct search to save time

    begin_set = set(wordList)  # words can be used from begin word direction
    end_set = set(wordList)  # words can be used from end word direction

    if endWord not in end_set:  # edge case
        return 0

    begin_level = set()  # the path level from begin word
    begin_level.add(beginWord)
    if beginWord in begin_set:
        begin_set.remove(beginWord)
    end_level = set()  # the path level from end word
    end_level.add(endWord)
    end_set.remove(endWord)

    seq = 1
    word_len = len(beginWord)

    while begin_level:
        # find a short layer to reduce the time
        if len(begin_level) > len(end_level):
            begin_level, end_level = end_level, begin_level
            begin_set, end_set = end_set, begin_set

        next_level = set()
        seq += 1
        for curr_word in begin_level:
            for i in range(0, word_len):
                for j in range(26):
                    if j == ord(curr_word[i]) - ord('a'):
                        continue
                    next_word = curr_word[0:i] + chr((ord('a') + j)) + curr_word[i + 1:]
                    if next_word not in begin_set:
                        continue

                    # if the next_word in begin_set but no in end_set, that means there's overlap for the nodes
                    # in other word, we find a path
                    if next_word not in end_set:
                        return seq

                    next_level.add(next_word)

        begin_level = next_level
        for word in next_level:
            begin_set.remove(word)

    return 0


# test cases
# print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))   # 5
print(ladderLength("a", "c", ["a", "b", "c"]))  # 2
print(ladderLength("ta", "if", ["ts", "sc", "ph", "ca", "jr", "hf", "to", "if", "ha", "is", "io", "cf", "ta"]))
