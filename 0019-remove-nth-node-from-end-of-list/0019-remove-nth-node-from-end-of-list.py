# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        
        if not head.next:
            return None
        
        end = head
        for i in range(n):
            end = end.next
          
        current = head
        prev = None
        while end:
            prev = current
            current = current.next
            end = end.next
            
        # if nth node from end is the first node
        if not prev:
            return head.next
        # if nth node from end is in middle
        if prev and current.next:
            prev.next = current.next
            return head
        # if nth node from end is at the end
        if not current.next:
            prev.next = None
            return head
            
        print('curr: ', current.val)
        print('prev: ', prev.val)
        
        return head
        
        