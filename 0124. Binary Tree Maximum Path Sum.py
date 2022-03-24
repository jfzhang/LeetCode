"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting
them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    def path_to_node(node) -> int:
        if not node:
            return 0

        left_path = max(path_to_node(node.left), 0)
        right_path = max(path_to_node(node.right), 0)

        nonlocal max_path
        max_path = max(max_path, node.val + left_path + right_path)

        return node.val + max(left_path, right_path)

    max_path = float("-inf")
    path_to_node(root)

    return max_path
