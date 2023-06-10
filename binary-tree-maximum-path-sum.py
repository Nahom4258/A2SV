# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxim = float('-inf')

        def dfs(node):
            nonlocal maxim

            if not node:
                return 0
            
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            
            maxim = max(maxim, node.val + left_sum + right_sum)
            
            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        
        return maxim