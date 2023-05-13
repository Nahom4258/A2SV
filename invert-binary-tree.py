# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ret = root

        def helper(root):
            if not root:
                return 

            temp_left = None
            temp_right = None

            if root.left:
                temp_left = root.left
            if root.right:
                temp_right = root.right

            root.left = temp_right
            root.right = temp_left

            helper(root.left)
            helper(root.right)

            return

        helper(root)

        return ret