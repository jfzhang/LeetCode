"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return root

    res = []

    def preorder(node):
        if not node:
            return

        res.append(node.val)
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return res
