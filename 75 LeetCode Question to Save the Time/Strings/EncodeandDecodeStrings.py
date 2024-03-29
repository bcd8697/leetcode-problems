'''
Description

Design an algorithm to encode a list of strings to a string. 
The encoded string is the sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example

Input: ['lint', 'code', 'love', 'you']
Output: ['lint', 'code', 'love', 'you']

Explanation:
One possible encode method is: 'lint:;code:;love:;you'

'''

class Solution:
  def encode(self, strs):
    res = ''
    for s in strs:
      res += str(len(s)) + '#' + s
    return res
  
  def decode(self, str):
    res, i= [], 0
    
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
      
        length = int(str[i:j])
        res.append(str[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res
      
        
