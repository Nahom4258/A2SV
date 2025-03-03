# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(curr, total):
            if not curr:
                return 0

            right_sum = helper(curr.right, total) + curr.val
            left_sum = helper(curr.left, total+right_sum)

            curr.val = right_sum + total

            return left_sum + right_sum

        if root.right:
            total_right_sum = helper(root.right, 0)
            root.val = total_right_sum + root.val

        if root.left:
            helper(root.left, root.val)

        return root