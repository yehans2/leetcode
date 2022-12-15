# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rab, tur = head, head
        
        while rab and rab.next:
            rab = rab.next.next
            tur = tur.next
        return tur