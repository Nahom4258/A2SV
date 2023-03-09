# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        new = TreeNode()

        def helper(root1, root2):
            if not root1 and not root2:
                return

            new_node = TreeNode()
            if root1 and root2:
                new_node.val = root1.val + root2.val
                new_node.left = helper(root1.left, root2.left)
                new_node.right = helper(root1.right, root2.right)
            elif root1 and not root2:
                new_node.val = root1.val
                new_node.left = helper(root1.left, None)
                new_node.right = helper(root1.right, None)
            elif not root1 and root2:
                new_node.val = root2.val
                new_node.left = helper(None, root2.left)
                new_node.right = helper(None, root2.right)

            return new_node

        return helper(root1, root2)