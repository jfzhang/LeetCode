"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255
(inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and
 "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots
into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
    1 <= s.length <= 20
    s consists of digits only
"""
from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    # Use Backtracking
    def backtrack(s: str, address: str, num: int):
        if num == 1:
            if not s or (s[0] == '0' and len(s) > 1) or int(s[::]) > 255:
                return
            res.append(address[1:] + '.' + s[:])
            return

        for i in range(min(3, len(s))):
            if (s[0] == '0' and i > 0) or int(s[0:i+1]) > 255 or len(s[i+1:]) > 3 * (num - 1):  # leading with 0
                continue
            backtrack(s[i + 1:], address + '.' + s[0:i+1], num - 1)

    res = []
    backtrack(s, "", 4)

    return res


# test cases
#print(restoreIpAddresses("25525511135"))  # ["255.255.11.135","255.255.111.35"]
#print(restoreIpAddresses("0000"))  # ["0.0.0.0"]
print(restoreIpAddresses("101023"))  # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
