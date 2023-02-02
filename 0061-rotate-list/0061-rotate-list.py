# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
            
        if size == 0:
            return head
        
        prev = None
        for i in range(k%size):
            curr = head
            while curr.next:
                prev = curr
                curr = curr.next

            curr.next = head
            head = curr
            prev.next = None
        
        return head