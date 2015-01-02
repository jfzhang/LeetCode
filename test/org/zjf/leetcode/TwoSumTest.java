package org.zjf.leetcode

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.zjf.leetcode.TwoSum;

public class TwoSumTest {

	private TwoSum twoSum;
	
	@Before
	public void setUp() {
		twoSum = new TwoSum();
	}
	
	@Test
	public void testTwoSum() {
		assertArrayEquals(null, twoSum.twoSum(new int[] {1}, 0));
	}

	@After
	public void tearDown() {
		twoSum = null;
	}
}
