# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 and not root2) or (root2 and not root1):
            return False
        
        def helper(n1, n2):
            # both are empty, means both reached the leaf node
            if not n1 and not n2:
                return True
            # if left has node but right doesn't; and vise-versa
            if (n1 and not n2) or (n2 and not n1):
                return False

            # check if curr are the same for n1 and n2, mainly for the root node
            if n1.val != n2.val:
                return False

            l, r = False, False
            if (n1.left and n2.left and n1.left.val == n2.left.val) or (not n1.left and not n2.left):
                l = helper(n1.left, n2.left)
                r = helper(n1.right, n2.right)
            elif (n1.left and n2.right and n1.left.val == n2.right.val) or (not n1.left and not n2.right):
                l = helper(n1.left, n2.right)
                r = helper(n1.right, n2.left)
            else:
                return False

            return l and r

        return helper(root1, root2)