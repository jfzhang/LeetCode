"""
Given the root of a binary tree, flatten the tree into a "linked list":
    * The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the
    list and the left child pointer is always null.
    * The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    """
    The challenge is not using O(1) space.
    It asks to use preorder traversal. Take root as example, the node visited before its left should be the "most right"
    leaf of its left child tree. So, The idea is moving the current node's whole right child tree to the "most right"
    leaf of its left child tree, then move its left child to the right child. Continue to next (right) node.
    """

    curr = root
    while curr:
        if curr.left:
            left, most_right = curr.left, curr.left
            while most_right.right:
                most_right = most_right.right
            most_right.right = curr.right
            curr.left = None
            curr.right = left
        curr = curr.right
