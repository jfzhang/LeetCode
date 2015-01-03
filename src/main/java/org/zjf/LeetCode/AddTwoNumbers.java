package org.zjf.LeetCode;

public class AddTwoNumbers {

	/*
	 * You are given two linked lists representing two non-negative numbers. The
	 * digits are stored in reverse order and each of their nodes contain a
	 * single digit. Add the two numbers and return it as a linked list. Input:
	 * (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8
	 */

	// Definition for singly-linked list.
	static class ListNode {
		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
			next = null;
		}
	}

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode head = null, node = null, next = null;
		int x=0, t=0;
		
		if (l1 == null && l2 == null)
			return null;
		
		if (l1 == null)
			return l2;
		
		if (l2 == null)
			return l1;
		
		node = new ListNode(0);
		head = node;
		
		while (l1 != null || l2 != null) {
			
			x = ((l1 == null) ? 0 : l1.val) + ((l2 == null) ? 0 : l2.val) + t;
			t = (int)(x/10);
			x -= t * 10;
			
			next = new ListNode(x);
			node.next = next;
			node = next;
			l1 = (l1 == null) ? null : l1.next;
			l2 = (l2 == null) ? null : l2.next;
		}
		
		if (t > 0) {
			next = new ListNode(t);
			node.next = next;
			node = next;
		}
		
		return head.next;
	}
}
