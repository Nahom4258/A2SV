# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        ans = []
        
        def helper(node, curr_sum, arr):
            if not node:
                return

            if not node.left and not node.right:
                if curr_sum+node.val == targetSum:
                    nonlocal ans
                    ans.append(arr+[node.val][::])

            helper(node.left, curr_sum+node.val, arr+[node.val])
            helper(node.right, curr_sum+node.val, arr+[node.val])

            return

        helper(root, 0, [])

        return ans