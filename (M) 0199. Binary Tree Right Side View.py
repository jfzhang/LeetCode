"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you
can see ordered from top to bottom.
"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    q = [root]

    while q:
        temp_q = q[:]
        res.append(q[-1].val)
        q.clear()

        for node in temp_q:
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res
