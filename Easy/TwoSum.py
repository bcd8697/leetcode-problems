''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. '''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        
        for i_idx, i in enumerate(nums):
            for j_idx, j in enumerate(nums):
                if i_idx == j_idx:
                    continue
                else:
                    if i + j == target:
                        res.append(i_idx)
                        res.append(j_idx)
                        break
        res = list(set(res))
        
        return res
                
                
            
