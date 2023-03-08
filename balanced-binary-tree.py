# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return True, 0

            flag, left_depth = depth(root.left)
            flag2, right_depth = depth(root.right)

            if flag and flag2 and abs(left_depth - right_depth) < 2:
                return True, max(left_depth, right_depth) + 1
            
            return False, 0
            

        return depth(root)[0]