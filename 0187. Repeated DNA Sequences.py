"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur
more than once in a DNA molecule. You may return the answer in any order.
"""
from collections import defaultdict
from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    seq_len = 10
    n = len(s)
    res = []

    if n <= seq_len:
        return res

    codes = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    x = 0
    for ch in s[:seq_len]:
        x = (x << 2) | codes[ch]
    counter = defaultdict(int)
    counter[x] += 1
    for i in range(n - seq_len):
        x = ((x << 2) | codes[s[seq_len + i]]) & ((1 << (seq_len * 2)) - 1)
        counter[x] += 1
        if counter[x] == 2:
            res.append(s[i + 1:i + seq_len + 1])

    return res


# test cases
print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))  # ["AAAAACCCCC","CCCCCAAAAA"]
