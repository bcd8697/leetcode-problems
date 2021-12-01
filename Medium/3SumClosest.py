'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dif = 2**31 - 1
        res = 0
        
        for i, a in enumerate(nums):
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum - target > 0:
                    r -= 1
                    if abs(threeSum - target) < dif:
                        dif = abs(threeSum - target)
                        res = threeSum
                elif threeSum - target < 0:
                    l += 1
                    if abs(threeSum - target) < dif:
                        dif = abs(threeSum - target)
                        res = threeSum
                else:
                    return threeSum
        return res
