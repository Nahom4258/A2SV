# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left, right):
            if not root:
                return True

            l = False
            r = False
            if left < root.val < right:
                l = helper(root.left, left, root.val)
            else:
                l = False
            
            if left < root.val < right:
                r = helper(root.right, root.val, right)
            else:
                r = False

            return l and r

        return helper(root, float('-inf'), float('inf'))