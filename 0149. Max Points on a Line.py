"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of
points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    All the points are unique.
"""
from collections import defaultdict
from typing import List
import math


def maxPoints(points: List[List[int]]) -> int:
    # the points on a line have the same slope
    n = len(points)
    if n < 3:
        return n

    ans = 0
    hash_map = defaultdict(int)

    for i in range(n):
        x1, y1 = points[i]
        hash_map.clear()
        if ans > n // 2 or ans > n - i:
            return ans

        for j in range(i + 1, n):
            x2, y2 = points[j]
            x, y = x1 - x2, y1 - y2
            if x == 0:
                y = 1
            elif y == 0:
                x = 1
            else:
                if y < 0:
                    x = -x
                    y = -y
                m = math.gcd(x, y)
                x, y = x // m, y // m

            hash_map[str([x, y])] += 1

        ans = max(ans, max(hash_map.values()) + 1)

    return ans


# test cases
print(maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4
print(maxPoints([[0, 0], [2, 2], [-1, -1]]))  # 3
