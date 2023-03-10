# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        counter = 0

        def helper(root):
            if not root:
                # return values - (sum, depth)
                return 0, 0

            left_sum, left_depth = helper(root.left)
            right_sum, right_depth = helper(root.right)

            # calculate average
            sum = root.val + left_sum + right_sum
            no_of_nodes = left_depth + right_depth + 1
            
            # check for condition
            if root.val == sum // no_of_nodes:
                nonlocal counter
                counter += 1

            # return values - (sum, depth)
            return left_sum + right_sum + root.val, left_depth + right_depth + 1

        helper(root)

        return counter