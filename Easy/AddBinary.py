'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        num1, num2 = [], []
        
        for i in reversed(a):
            num1.append(int(i))
        for i in reversed(b):
            num2.append(int(i))
            
        size = max(len(num1), len(num2))
        
        num1 += [0] * (size - len(num1))
        num2 += [0] * (size - len(num2))
        
        print (num1, num2)
        
        overflow = 0
        res = []
    
        for obj in zip(num1, num2):
            value = obj[0] + obj[1] + overflow
            overflow = value // 2
            res.append(value % 2)
            
        if overflow == 1:
            res.append(1)
            
        res = res[::-1]

        return ''.join(map(str, res))

        
