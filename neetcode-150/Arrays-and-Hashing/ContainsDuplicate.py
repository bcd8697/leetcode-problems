'''
https://leetcode.com/problems/contains-duplicate/
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        unique = set()
        
        for n in nums:
            if n not in unique:
                unique.add(n)
            else:
                return True
        
        return False
