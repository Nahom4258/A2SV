# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:                
        if not head or not head.next:
            return head
        
        new_head = ListNode(101, head)
        temp = new_head
        
        while new_head.next and new_head.next.next:
            curr = new_head.next.next
            
            if new_head.next.val == curr.val:
                if curr.next:
                    while curr and curr.next and curr.val == curr.next.val:
                        curr = curr.next
                new_head.next = curr.next
            else:
                new_head= new_head.next
            
        return temp.next
            
        