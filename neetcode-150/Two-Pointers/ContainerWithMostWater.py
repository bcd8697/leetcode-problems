'''
https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        biggest = 0
        
        l = 0
        r = len(height) - 1
        
        while l != r or r < l:
            square = (r - l) * min(height[l], height[r])
            
            if biggest < square:
                biggest = square      
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1 
        
        return biggest
