'''Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            a = str(x)
            b = a[::-1]
            b = b[:-1]
            b = '-' + b
        else:
            a = str(x)
            b = a[::-1]
        
        res = int(b)
        
        if res > 2**31 - 1 or res < -2**31:
            res = 0
            
        return res
