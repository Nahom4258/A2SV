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
        
        def helper(node, ans):
            if not node:
                return None

            node.left = helper(node.left, ans)
            node.right = helper(node.right, ans)

            if node.val in to_del:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return None

            return node

        if root.val not in to_del:
            ans.append(root)

        helper(root, ans)

        return ans