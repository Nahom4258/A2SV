# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode(-1000)
        cphead = newhead
        
        def helper(list1, list2, cphead):
            if not list1 and not list2:
                return newhead.next
            
            if list1 and list2:
                if list1.val < list2.val:
                    temp = list1.next
                    cphead.next = list1
                    return helper(temp, list2, cphead.next)
                else:
                    temp = list2.next
                    cphead.next = list2
                    return helper(list1, temp, cphead.next)
            else:
                if list1:
                    temp = list1.next
                    cphead.next = list1
                    return helper(temp, list2, cphead.next)
                else:
                    temp = list2.next
                    cphead.next = list2
                    return helper(list1, temp, cphead.next)
                    
        return helper(list1, list2, cphead)