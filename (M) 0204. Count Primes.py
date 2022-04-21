"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""


def countPrimes(n: int) -> int:
    if n < 2:
        return 0

    flag = [1] * n
    res = 0

    for i in range(2, n):
        if flag[i]:
            res += 1

            j = i * i
            while j < n:
                flag[j] = 0
                j += i

    return res


# test cases
print(countPrimes(10))  # 4
