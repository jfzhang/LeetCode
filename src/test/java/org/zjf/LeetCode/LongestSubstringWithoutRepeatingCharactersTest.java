package org.zjf.LeetCode;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class LongestSubstringWithoutRepeatingCharactersTest {

	private LongestSubstringWithoutRepeatingCharacters longestSub;

	@Before
	public void setUp() {
		longestSub = new LongestSubstringWithoutRepeatingCharacters();
	}

	@Test
	public void testLengthOfLongestSubstringZero() {
		assertEquals(0, longestSub.lengthOfLongestSubstring(null));
		assertEquals(0, longestSub.lengthOfLongestSubstring(""));
	}
	
	@Test
	public void testLengthOfLongestSubstringOne() {
		assertEquals(1, longestSub.lengthOfLongestSubstring("a"));
	}
	
	@Test
	public void testLengthOfLongestSubstringOneRepeat() {
		assertEquals(1, longestSub.lengthOfLongestSubstring("aaaaaaaaaaaaaaaaa"));
	}
	
	@Test
	public void testLengthOfLongestSubstringNoRepeat() {
		assertEquals(26, longestSub.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz"));
	}
	
	@Test
	public void testLengthOfLongestSubstring1() {
		assertEquals(3, longestSub.lengthOfLongestSubstring("abccba"));
		assertEquals(4, longestSub.lengthOfLongestSubstring("abccdba"));
	}

	@After
	public void tearDown() {
		longestSub = null;
	}

}
