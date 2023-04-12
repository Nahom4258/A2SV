# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []

        def helper(head, path):
            if not head.left and not head.right:
                paths.append(int(''.join(path[::]+[str(head.val)])))
                return

            if head.left:
                helper(head.left, path+[str(head.val)])
            if head.right:
                helper(head.right, path+[str(head.val)])

            return

        helper(root, [])

        return sum(paths)