"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the
Hamming weight).
"""


def hammingWeight(n: int) -> int:
    res = 0
    for i in range(32):
        if n & 1:
            res += 1
        n >>= 1

    return res