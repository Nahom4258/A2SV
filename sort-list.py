# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        left, right = self.splitMiddle(head)
        left_small = self.sortList(left)
        right_small = self.sortList(right)

        return self.mergeSort(left_small, right_small)

        return helper(head)

    def splitMiddle(self, head):
        left = right = head

        while right and right.next:
            left = left.next
            right = right.next.next

        right = head

        while right:
            if right.next == left:
                break
            right = right.next

        right.next = None

        return head, left

    def mergeSort(self, head1, head2):
        ret_head = ListNode()
        current = ret_head

        while head1 or head2:
            if head1 and head2:
                if head1.val <= head2.val:
                    current.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    current.next = ListNode(head2.val)
                    head2 = head2.next
            elif head1:
                current.next = ListNode(head1.val)
                head1 = head1.next
            elif head2:
                current.next = ListNode(head2.val)
                head2 = head2.next
            
            current = current.next

        return ret_head.next