package org.zjf.leetcode;

import java.util.HashMap;

public class TwoSum {
	/*
	 * Given an array of integers, find two numbers such that they add up to a
	 * specific target number. The function twoSum should return indices of the
	 * two numbers such that they add up to the target, where index1 must be
	 * less than index2. Please note that your returned answers (both index1 and
	 * index2) are not zero-based. You may assume that each input would have
	 * exactly one solution.
	 * 
	 * Input: numbers={2, 7, 11, 15}, target=9 Output: index1=1, index2=2
	 */

	public int[] twoSum(int[] numbers, int target) {

		// Use a hash map that maps a value to its index.
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int i = 0; i < numbers.length; i++) {
			map.put(numbers[i], i);
		}

		for (int i = 0; i < numbers.length; i++) {
			Integer j = map.get(target - numbers[i]);

			/*
			 * Check (target - numbers[i]) exists in hash map, and two numbers
			 * are different numbers in the array e.g. numbers={3, 2, 4},
			 * target=6, avoid to output [1,1];
			 */
			if (j != null && j != i) {
				return new int[] { i + 1, j + 1 };
			}
		}

		return null;
	}
}
