# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res, tmp = head, head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        tmp = ListNode(0)
        for i in range(count):
            if i == count - n:
                head = head.next
                continue
            ptr = tmp
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(head.val)
            head = head.next
        return tmp.next
        