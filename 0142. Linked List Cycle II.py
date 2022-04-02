"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    slow, fast = head, head
    while fast:
        slow = slow.next
        if not fast.next:
            return None
        fast = fast.next.next
        if slow == fast:
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return slow

    return None
