# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Author : Prasaanth Selvakumar
# Date : 04/11/2021

"""
##Problem
Given a string s, find the length of the longest substring without repeating characters.



####Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

####Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

####Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

####Example 4:

Input: s = ""
Output: 0



###Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos_dict = {}
        max_len = 0
        prev_l_ind = 0
        ind = -1
        for ind, char in enumerate(s):
            if pos_dict.get(char, None) is not None:
                if (max_len < (ind - prev_l_ind)):
                    max_len = (ind - prev_l_ind)
                np = pos_dict[char] + 1
                prev_l_ind = np if (prev_l_ind < np) else prev_l_ind
            pos_dict[char] = ind
        if (max_len < (ind - prev_l_ind + 1)):
            max_len = ind - prev_l_ind + 1
        return max_len
