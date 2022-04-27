'''
https://leetcode.com/problems/top-k-frequent-elements/
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
    
        d = Counter(d)
        
        res = []
        
        for _, (key, value) in zip(range(k), d.most_common()):
            res.append(key)
        
        return res
