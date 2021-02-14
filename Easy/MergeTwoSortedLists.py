'''Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:     
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res = []
        
        ### for l1
        if l1:
            printval = l1.val
            nextnode = l1.next

            while nextnode is not None:
                res.append(printval)
                printval = nextnode.val
                nextnode = nextnode.next

            res.append(printval)
        
        ### for l2
        if l2:
            printval = l2.val
            nextnode = l2.next

            while nextnode is not None:
                res.append(printval)
                printval = nextnode.val
                nextnode = nextnode.next

            res.append(printval)
        
        res = sorted(res)
        
        # converting List to ListNode
        if l1 or l2:
            head = ListNode(res[0])
            tail = head
            e = 1

            while e < len(res):
                tail.next = ListNode(res[e])
                tail = tail.next
                e += 1

            res_ll = head
        
        else:
            res_ll = ListNode(None)
            return res_ll.val
        
        return res_ll
