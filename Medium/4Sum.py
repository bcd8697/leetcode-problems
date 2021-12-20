'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(nums)
        nums = sorted(nums)
        s = 0
        
        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
            
                left = j + 1
                right = n - 1
            
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s > target:
                        right -= 1

                    elif s == target:
                        t = []
                        t.append(nums[i])
                        t.append(nums[j])
                        t.append(nums[left])
                        t.append(nums[right])

                        res.append(t)

                        left += 1

                    else:
                        left += 1

        ans = list(set(tuple(i) for i in res))
        
        return ans
