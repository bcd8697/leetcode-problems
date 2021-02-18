'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        
        l_h, l_n = [], []
        
        for i in haystack:
            l_h.append(i)
        
        for i in needle:
            l_n.append(i)
            
        # supposing that len(needle) < len(haystack)
        for i in range(len(l_h)):
            if l_h[i:i+len(l_n)] == l_n:
                print('found')
                return i
            
        return -1
