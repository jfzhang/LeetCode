"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    ans = float("inf")
    if root.left:
        ans = min(minDepth(root.left), ans)
    if root.right:
        ans = min(minDepth(root.right), ans)

    return ans + 1
