package org.zjf.LeetCode;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class TwoSumTest {

	private TwoSum twoSum;

	@Before
	public void setUp() {
		twoSum = new TwoSum();
	}

	@Test
	public void testTwoSum() {
		assertArrayEquals(null, twoSum.twoSum(new int[] { 1 }, 0));

		assertArrayEquals(new int[] {2,3}, twoSum.twoSum(new int[] {3,2,4}, 6));
	}

	@After
	public void tearDown() {
		twoSum = null;
	}
}
