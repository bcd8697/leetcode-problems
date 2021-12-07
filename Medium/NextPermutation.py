'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        if n == 1:
            return
        
        i = 1
        lastInc = -1
        
        # Finding the peark of ASCENDING order
        while i < n:
            if nums[i] > nums[i-1]:
                lastInc = i
            i += 1
        
        print(lastInc)
        
        # Checking if array is DESCENDING
        if lastInc == -1:
            nums = nums.sort()
            return
        
        # Finding element in range 
        # (nums[lastInc - 1], nums[lastInc]) to the right
        mn = nums[lastInc]
        index = lastInc
        for i in range(lastInc, n):
            if nums[i] > nums[lastInc - 1] and nums[i] < nums[index]:
                index = i
            
        nums[lastInc - 1], nums[index] = nums[index], nums[lastInc - 1]
        nums[lastInc:] = sorted(nums[lastInc:])
