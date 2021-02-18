'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        s = 0
        s_list = []
      
        for i_idx, i in enumerate(nums):
            s += i
            s_list.append(s)
            
            if s < 0:
                s = 0
            
        return max(s_list)
                
