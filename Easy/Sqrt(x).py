'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        
        x = str(x**0.5)
        
        for idx, i in enumerate(x):
            if i == '.':
                dot_idx = idx
                return int(x[:idx])

