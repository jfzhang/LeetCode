"""
Reverse bits of a given 32 bits unsigned integer.
"""


def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1

    return res
