"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as: a binary tree in which the left and right subtrees of
every node differ in height by no more than 1.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    # Use postorder traversal that can go from bottom to top and reduce the time complexity to O(n)
    # -1 means not balanced
    if not root:
        return True

    def getTreeLevel(root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_level = getTreeLevel(root.left)
        right_level = getTreeLevel(root.right)
        if left_level == -1 or right_level == -1 or abs(left_level - right_level) > 1:
            return -1

        return max(left_level, right_level) + 1

    return getTreeLevel(root) > 0
