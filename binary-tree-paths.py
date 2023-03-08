# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        total = []

        def helper(root, ans):
            if not root:
                return

            if not root.left and not root.right:
                copy = ans[::]
                copy.append(root.val)
                total.append('->'.join(list(map(str, copy))))
                return

            ans.append(root.val)
            helper(root.left, ans)
            helper(root.right, ans)
            if ans: ans.pop()

        helper(root, ans)

        return total