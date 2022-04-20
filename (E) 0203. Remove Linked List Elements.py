"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return head

    dummy = ListNode(0, head)
    pre, node = dummy, head
    while node:
        if node.val == val:
            pre.next = node.next
        else:
            pre = pre.next
        node = pre.next

    return dummy.next
