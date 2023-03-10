# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        column = defaultdict(list)

        def helper(root, row, col):
            if not root:
                return

            # ans.append((root.val, row, col))
            column[col].append([root.val, row])
            helper(root.left, row + 1, col - 1)
            helper(root.right, row + 1, col + 1)

        helper(root, 0, 0)

        sorted_keys = sorted(column.keys())
        for key in sorted_keys:
            curr = column[key]
            curr.sort(key=lambda x: (x[1], x[0]))
            ans.append([num[0] for num in curr])

        return ans