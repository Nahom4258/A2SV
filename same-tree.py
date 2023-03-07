# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorder(p) == self.inorder(q)

    def inorder(self, root):
        ans = []

        def f(root):
            if not root:
                return
            if not root.left:
                ans.append(None)
            if not root.right:
                ans.append(None)

            f(root.left)
            ans.append(root.val)
            f(root.right)

        f(root)

        return ans