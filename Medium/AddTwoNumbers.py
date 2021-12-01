'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_str = ''
        l2_str = ''
        
        # check if there only 1 number in linked lists
        if l1.next == None:
            l1_str += str(l1.val)
        
        if l2.next == None:
            l2_str += str(l2.val)
        
        # unpacking linked list 1 
        while l1.next != None:
            l1_str += str(l1.val)
            l1 = l1.next
            
            # adding final value of the linked list to the string
            if l1.next == None:
                l1_str += str(l1.val)
                l1_str = l1_str[::-1]
        
        # unpacking linked list 2
        while l2.next != None:
            l2_str += str(l2.val)
            l2 = l2.next
            # adding final value of the linked list to the string
            if l2.next == None:
                l2_str += str(l2.val)
                l2_str = l2_str[::-1]
        
        # summing up
        twoSum = list(str(int(l1_str) + int(l2_str))[::-1])
        
        # creating linked list to return
        head = ListNode(twoSum[0])
        tail = head
        e = 1
        
        while e < len(twoSum):
            tail.next = ListNode(twoSum[e])
            tail = tail.next
            e+=1
        
        return head
