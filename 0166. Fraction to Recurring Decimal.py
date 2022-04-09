"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 4, denominator = 333
Output: "0.(012)"

Constraints:
    -231 <= numerator, denominator <= 231 - 1
    denominator != 0
"""


def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator % denominator == 0:
        return str(numerator // denominator)

    res = []
    if numerator * denominator < 0:
        res.append("-")
    numerator = abs(numerator)
    denominator = abs(denominator)
    res.append(str(numerator // denominator))
    res.append(".")

    remainder = numerator % denominator
    frac_pos = {}
    while remainder > 0 and remainder not in frac_pos:
        frac_pos[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator

    if remainder:
        idx = frac_pos[remainder]
        res.insert(idx, "(")
        res.append(")")

    return "".join(res)


# test cases
print(fractionToDecimal(1, 2))  # 0.5
print(fractionToDecimal(4, 333))  # 0.(012)
