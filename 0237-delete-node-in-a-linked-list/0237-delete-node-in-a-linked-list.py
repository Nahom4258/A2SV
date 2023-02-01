# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        following = node.next
        while following:
            node.val, following.val = following.val, node.val
            if not following.next:
                node.next = None
                break
            node = node.next
            following = following.next