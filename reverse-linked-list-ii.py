# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_head = ListNode(0)
        new_head.next = head
        prev = new_head

        for i in range(1, left):
            prev = prev.next

        start = prev.next
        curr = start.next
        for i in range(left, right):
            start.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = start.next
        
        return new_head.next