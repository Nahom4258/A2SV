# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ''
        
        def helper(head):
            nonlocal string

            if not head:
                return None

            string += str(head.val)

            if head.left:
                string += '('
                helper(head.left)
                string += ')'

            if not head.left and head.right:
                string += '()'
                
            if head.right:
                string += '('
                helper(head.right)
                string += ')'
            
            return head.val

        helper(root)

        return string