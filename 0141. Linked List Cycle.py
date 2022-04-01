"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(self, head: Optional[ListNode]) -> bool:
    # use two points, one slow, one fast
    if not head or not head.next:
        return False

    s, f = head, head.next
    while s != f:
        if not f or not f.next:
            return False
        s = s.next
        f = f.next.next

    return True
