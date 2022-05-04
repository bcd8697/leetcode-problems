'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

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
