'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
nums is a non-decreasing array.
-10**9 <= target <= 10**9
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums) - 1
        
        leftIdx = -1
        rightIdx = -1
        
        while l <= r:
            
            # every loop we check if we found the solution during the previous loop
            if nums[l] == nums[r] == target:
                leftIdx = l
                rightIdx = r
                break
            
            # left pointer moving
            if nums[l] != target:
                l += 1
            else:
                leftIdx = l
            
            # right pointer moving
            if nums[r] != target:
                r -= 1
            else:
                rightIdx = r
                
        return [leftIdx, rightIdx]
