# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        graph = defaultdict(list)
        ans = 0
        visited = set()
        add = []

        def helper(head, depth):
            if not head:
                return
            if depth == 2:
                if head not in visited:
                    nonlocal ans
                    ans += head.val
                    add.append(head.val)
                return

            helper(head.left, depth+1)
            helper(head.right, depth+1)

            return

        def dfs(head):
            if not head:
                return

            if head.val % 2 == 0:
                helper(head, 0)

            dfs(head.left)
            dfs(head.right)

            return

        dfs(root)
        # print('ans: ', ans)
        # print('arr: ', add)

        return ans