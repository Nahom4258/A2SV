# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        
        current = l1
        while current:
            num1 += str(current.val)
            current = current.next
        current = l2
        while current:
            num2 += str(current.val)
            current = current.next
            
        num2 = str(int(num1[::-1]) + int(num2[::-1]))
        num2 = num2[::-1]
        
        head = ListNode(num2[0])
        current = head
        for i in range(1, len(num2)):
            current.next = ListNode(num2[i])
            current = current.next
            
        return head