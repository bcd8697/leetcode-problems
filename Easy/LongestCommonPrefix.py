'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ''

        if len(strs) != 0:    
            prefix = strs[0]

            for string in strs[1:]:
                while string[:len(prefix)] != prefix and prefix:
                    prefix = prefix[:len(prefix)-1]

                if not prefix:
                    break
                    
            res = prefix
        
        return res
