# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # find the middle
        mid_prev = head
        while fast and fast.next:
            mid_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # end linked list before middle
        mid_prev.next = None
        
        # reverse linked list after middle
        mid = slow
        prev = None
        foll = slow
        while mid:
            foll = foll.next
            mid.next = prev
            prev = mid
            mid = foll
        new_head = prev
        
        # check left and right linked list
        left = head
        right = new_head
        palindrome = True
        while left:
            if left.val != right.val:
                palindrome = False
                break
            left = left.next
            right = right.next
        
        return palindrome