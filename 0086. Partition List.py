"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
 than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    if not head:
        return head

    large_head = ListNode(0)
    large_node = large_head
    small_head = ListNode(0)
    small_node = small_head

    while head:
        if head.val < x:
            small_node.next = head
            small_node = head
        else:
            large_node.next = head
            large_node = head
        head = head.next

    small_node.next = large_head.next
    large_node.next = None

    return small_head.next
