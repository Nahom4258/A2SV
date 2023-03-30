# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        print(arr)

        maxim = -1
        for i in range(len(arr)//2):
            maxim = max(maxim, arr[i] + arr[(len(arr)-1-i)])

        return maxim