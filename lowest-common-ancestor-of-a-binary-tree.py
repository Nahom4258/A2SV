# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root:
                return False, 0
            if root.val == p.val or root.val == q.val:
                return True, root

            left, val = helper(root.left, p, q)
            right, val2 = helper(root.right, p, q)

            if not left and not right:
                return False, 0
            if (not left and right) or (not right and left):
                return True, (val if left else val2)
            if left and right:
                return True, root

        return helper(root, p, q)[1]