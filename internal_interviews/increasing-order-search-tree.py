# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nums = []
        
        def helper(node):
            if not node:
                return

            helper(node.left)
            nums.append(node.val)
            helper(node.right)

            return

        helper(root)
        
        dummy = TreeNode(-1)
        
        temp = dummy
        for i in range(len(nums)):
            temp.right = TreeNode(nums[i])
            temp = temp.right

        return dummy.right