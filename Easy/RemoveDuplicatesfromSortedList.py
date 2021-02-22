'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3] 

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # if the list is empty
        if not head:
            return ListNode(None).val
        
        ###########################
        
        res = []
        
        val = head.val
        nextnode = head.next
        
        while nextnode is not None:
            if val not in res:
                res.append(val)
                val = nextnode.val
                nextnode = nextnode.next
            elif val in res:
                val = nextnode.val
                nextnode = nextnode.next
            
        # check last value of the list
        if val not in res:
            res.append(val)
        
        # converting List to ListNode
        head = ListNode(res[0])
        tail = head
        e = 1

        while e < len(res):
            tail.next = ListNode(res[e])
            tail = tail.next
            e += 1

        res_ll = head
        
        return res_ll
