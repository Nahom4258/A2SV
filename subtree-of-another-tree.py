# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            ans = self.check_subtree(root, subRoot)

            if ans:
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check_subtree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if (not root and subRoot) or (not subRoot and root) or (root.val != subRoot.val):
            return False

        return self.check_subtree(root.left, subRoot.left) and self.check_subtree(root.right, subRoot.right)