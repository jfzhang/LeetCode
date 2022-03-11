"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:

    dummy_head = ListNode(0, head)
    pre = dummy_head
    node = pre.next

    while node and node.next:
        if node.val == node.next.val:
            value = node.val
            while node and node.val == value:
                pre.next = node.next
                node = node.next
        else:
            pre = node
            node = node.next

    return dummy_head.next


# test cases
#[1,2,3,3,4,4,5] --> [1,2,5]
head = ListNode(1)
node1 = head
for i in [2,3,3,4,4,5]:
    node2 = ListNode(i)
    node1.next = node2
    node1 = node2
print(deleteDuplicates(head))

