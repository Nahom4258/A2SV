# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def helper(node, parent):
            if not node:
                return

            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)
            if parent != -1:
                graph[node.val].append(parent)

            helper(node.left, node.val)
            helper(node.right, node.val)

            return

        helper(root, -1)

        ans = []
        def dfs(val, depth, parent):
            if depth == k:
                nonlocal ans
                ans.append(val)
                return

            for ch in graph[val]:
                if ch != parent:
                    dfs(ch, depth+1, val)

            return

        dfs(target.val, 0, -1)

        return ans