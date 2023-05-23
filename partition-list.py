# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start = head
        less = []
        great = []
        
        while start:
            if start.val < x:
                less.append(start.val)
            else:
                great.append(start.val)
            start = start.next

        less_counter = 0
        great_counter = 0
        less_size = len(less)
        great_size = len(great)

        while head and less_counter < less_size:
            head.val = less[less_counter]
            head = head.next
            less_counter += 1
        while head and great_counter<great_size:
            head.val = great[great_counter]
            head = head.next
            great_counter += 1
        return dummy.next