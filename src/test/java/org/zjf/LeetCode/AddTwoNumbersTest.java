package org.zjf.LeetCode;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.zjf.LeetCode.AddTwoNumbers.ListNode;

public class AddTwoNumbersTest {

	private AddTwoNumbers addTwoNumbers;

	@Before
	public void setUp() {
		addTwoNumbers = new AddTwoNumbers();
	}

	@Test
	public void testAddTwoNumbersBothNull() {
		assertEquals(null, addTwoNumbers.addTwoNumbers(null, null));
	}

	@Test
	public void testAddTwoNumbersOneNull() {
		ListNode l1 = new ListNode(1);
		l1.next = new ListNode(2);
		l1.next.next = new ListNode(3);

		ListNode r = addTwoNumbers.addTwoNumbers(l1, null);
		while (r != null) {
			assertEquals(l1.val, r.val);
			l1 = l1.next;
			r = r.next;
		}
	}

	@Test
	public void testAddTwoNumbersNormal() {
		ListNode l1 = new ListNode(1);
		l1.next = new ListNode(8);

		ListNode l2 = new ListNode(0);

		ListNode r = addTwoNumbers.addTwoNumbers(l1, l2);

		assertEquals(r.val, 1);
		assertEquals(r.next.val, 8);
	}
	
	@Test
	public void testAddTwoNumbersLarge() {
		ListNode l1 = new ListNode(9);
		l1.next = new ListNode(9);

		ListNode l2 = new ListNode(9);

		ListNode r = addTwoNumbers.addTwoNumbers(l1, l2);

		assertEquals(r.val, 8);
		assertEquals(r.next.val, 0);
		assertEquals(r.next.next.val, 1);
	}

	@After
	public void tearDown() {
		addTwoNumbers = null;
	}
}
