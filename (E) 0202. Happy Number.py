"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
    include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


def isHappy(n: int) -> bool:
    visited = set()

    while n not in visited and n != 1:
        visited.add(n)
        a = 0
        while n >= 10:
            a += (n % 10) ** 2
            n = n // 10
        n = a + n ** 2

    return True if n == 1 else False


# test cases
print(isHappy(19))  # True