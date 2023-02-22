# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if head and not head.next:
            return [0]

        ans = []
        stack = []
        
        lptr = None
        mptr = head
        rptr = head.next
        
        while rptr:
            mptr.next = lptr
            lptr = mptr
            mptr = rptr
            rptr = rptr.next
            
        mptr.next = lptr
        
        while mptr:
            if (len(stack) == 0):
                ans.append(0)
                stack.append(mptr.val);
         
            else:
                while (len(stack) != 0 and stack[-1]<= mptr.val):
                    stack.pop();
  
                if (len(stack) == 0):
                    ans.append(0)
                    stack.append(mptr.val)
             
                else:
                    ans.append(stack[-1])
                    stack.append(mptr.val)
            mptr = mptr.next
        
        return reversed(ans)
            
        
        