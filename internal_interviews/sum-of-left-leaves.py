# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, d):
            if not node:
                return 0

            left = helper(node.left, True)
            right = helper(node.right, False)

            if d and not node.left and not node.right:
                return left + right + node.val

            return left + right

        return helper(root, False)