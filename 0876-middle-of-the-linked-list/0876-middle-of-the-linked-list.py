# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left_ptr = head
        right_ptr = head
        
        while right_ptr and right_ptr.next:
            left_ptr = left_ptr.next
            right_ptr = right_ptr.next.next
            
        return left_ptr
        