package org.zjf.LeetCode;

public class LongestSubstringWithoutRepeatingCharacters {
	/*
	 * Given a string, find the length of the longest substring without
	 * repeating characters. For example, the longest substring without
	 * repeating letters for "abcabcbb" is "abc", which the length is 3. For
	 * "bbbbb" the longest substring is "b", with the length of 1.
	 */
	public int lengthOfLongestSubstring(String s) {
		if (s == null || s.isEmpty())
			return 0;

		if (s.length() == 1)
			return 1;

		int max = 0, start = 0;
		char[] arr = s.toCharArray();
		int[] hash = new int[255];
		
		for (int i=0; i<arr.length; i++)
		{
			if (hash[arr[i]] > 0) {
				max = Math.max(max, i-start);
				int p = hash[arr[i]];
				if (arr.length - p <= max)
					return max;
				
				for (int j=start; j<p; j++) {
					hash[arr[j]] = 0;
				}				
				start = p;
			}
			hash[arr[i]] = i+1;
		}

		return Math.max(max, arr.length-start);
	}
}
