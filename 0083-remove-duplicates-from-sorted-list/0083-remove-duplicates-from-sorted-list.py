# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = 101
        temp_node = None
        current = head
        
        while current:
            if temp != current.val:
                
                if not temp_node:
                    temp_node = current
                else:
                    temp_node.next = current
                    
                temp = current.val
                temp_node = current
            elif temp == current.val and not current.next:
                temp_node.next = None
                
            current = current.next
            
        return head