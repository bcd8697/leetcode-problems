'''
https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums)) # predefine an array to return
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
                
        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
    
