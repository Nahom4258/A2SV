# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found = False

        if not root:
            return False

        def dfs(root, sum):
            if not root:
                return

            if not root.left and not root.right:
                if sum+root.val == targetSum:
                    nonlocal found
                    found = True
                return

            dfs(root.left, sum+root.val)
            dfs(root.right, sum+root.val)

            return

        dfs(root, 0)

        return found