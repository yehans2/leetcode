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

	# def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	# ptr, length = head, 0
	# while ptr:
	# 	ptr, length = ptr.next, length + 1
	# if length == n : return head.next
	# ptr = head
	# for i in range(1, length - n):
	# 	ptr = ptr.next
	# ptr.next = ptr.next.next
	# return head