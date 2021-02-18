'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for idx, i in enumerate(nums):
            
            if i == target:
                return idx
            
            elif nums[idx-1] < target and target < nums[idx]:
                return idx
            
            elif idx == 0 and nums[idx] > target:
                return 0
            
            elif idx == len(nums)-1 and target > nums[idx]:
                return idx+1
                
