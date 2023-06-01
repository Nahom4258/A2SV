# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = dict()

        def dp(node):
            if not node:
                return 0

            if not node.left and not node.right:
                return node.val

            if node.left and node.right:
                if node not in memo:
                    memo[node] = max(node.val + dp(node.left.left) + dp(node.left.right) + dp(node.right.left) + dp(node.right.right), dp(node.left) + dp(node.right))
            elif node.left:
                if node not in memo:
                    memo[node] = max(node.val + dp(node.left.left) + dp(node.left.right), dp(node.left))
            elif node.right:
                if node not in memo:
                    memo[node] = max(node.val + dp(node.right.right) + dp(node.right.left), dp(node.right))

            return memo[node]

        return dp(root)