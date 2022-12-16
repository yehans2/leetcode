# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mul = 1
        res = 0
        n = res_node = ListNode(0)
        while l1 or l2:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            res += v1*mul + v2*mul
            mul *= 10
            
        res = list(str(res))
        while res:
            res_node.next = ListNode(res[-1])
            res.pop()
            res_node = res_node.next
        return n.next
       