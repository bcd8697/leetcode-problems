Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        longest = 0
        unique_set = set()
        
        while right < len(s):
            if s[right] not in unique_set:
                unique_set.add(s[right])
                
                right += 1
                
                longest = max(longest, len(unique_set))
            
            else:
                unique_set.remove(s[left])
                
                left += 1
                
        return longest
                
                
        
