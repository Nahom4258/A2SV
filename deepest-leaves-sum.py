# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        bfs = defaultdict(list)

        def dfs(node, index):
            if not node:
                return

            bfs[index].append(node.val)
            dfs(node.left, index+1)
            dfs(node.right, index+1)

            return

        dfs(root, 0)

        # print('ans; ', bfs)

        return sum(bfs[max(bfs.keys())])