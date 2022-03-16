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
