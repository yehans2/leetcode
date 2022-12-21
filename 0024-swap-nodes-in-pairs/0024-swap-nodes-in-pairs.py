# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0)
        tmp.next = head
        res = tmp
        while tmp.next and tmp.next.next:
            a = tmp.next
            b = a.next
            
            tmp.next, b.next, a.next = b, a, b.next
            
            tmp = a
        return res.next
        
            