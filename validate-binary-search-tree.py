# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.inorder(root)

        return ans == sorted(ans) and len(set(ans)) == len(ans)
    
    def inorder(self, root):
        ans = []

        def f(root):
            if not root:
                return

            f(root.left)
            ans.append(root.val)
            f(root.right)

        f(root)

        return ans