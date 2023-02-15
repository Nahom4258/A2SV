# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        left_ptr = head
        right_ptr = head
        
        while left_ptr and right_ptr and right_ptr.next:
            right_ptr = right_ptr.next.next
            left_ptr = left_ptr.next
            
            if right_ptr == left_ptr:
                right_ptr = head
                
                while right_ptr != left_ptr:
                    right_ptr = right_ptr.next
                    left_ptr = left_ptr.next
                    
                return left_ptr
        
        return None