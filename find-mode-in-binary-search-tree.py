# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = Counter(self.inorder(root))
        res = []
        maxim = max(ans.values())
        # print('max: ', max(ans.values()))
        for key in ans:
            if ans[key] == maxim:
                res.append(int(key)) 

        return res

    def inorder(self, root):
        ans = []

        def helper(root):
            if not root:
                return

            helper(root.left)
            ans.append(root.val)
            helper(root.right)

        helper(root)

        return ans