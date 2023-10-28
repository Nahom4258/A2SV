# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del = set(to_delete)
        ans = []
        
        def helper(node):
            if node.val in to_del:
                nonlocal ans
                if node.left and node.left.val not in to_del:
                    ans.append(node.left)
                if node.right and node.right.val not in to_del:
                    ans.append(node.right)

            if node.left:
                helper(node.left)
                if node.left.val in to_del:
                    node.left = None
            if node.right:
                helper(node.right)
                if node.right.val in to_del:
                    node.right = None

        if root.val not in to_del:
            ans.append(root)

        helper(root)

        return ans