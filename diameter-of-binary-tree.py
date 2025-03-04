# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def helper(curr):
            # If no nodes, return 0 as start of level
            if not curr:
                return 0

            left_max = helper(curr.left)
            right_max = helper(curr.right)

            nonlocal max_diameter
            max_diameter = max(max_diameter, left_max + right_max)

            return max(left_max, right_max) + 1

        helper(root)

        return max_diameter