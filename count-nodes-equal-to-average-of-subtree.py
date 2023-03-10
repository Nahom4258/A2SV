# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        arr = []
        counter = 0

        def helper(root):
            if not root:
                # return values - (sum, depth)
                return 0, 0

            left_sum, left_depth = helper(root.left)
            right_sum, right_depth = helper(root.right)
            arr.append([root.val, left_sum + right_sum, left_depth + right_depth + 1])

            # return values - (sum, depth)
            return left_sum + right_sum + root.val, left_depth + right_depth + 1

        helper(root)

        for vals in arr:
            val, sums, depth = vals
            if val == (sums + val) // depth:
                counter += 1

        return counter