# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def helper(node, parent):
            if not node:
                return

            if parent:
                graph[node.val].append(parent)
            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)

            helper(node.left, node.val)
            helper(node.right, node.val)

            return

        helper(root, None)
        
        queue = deque([start])
        visited = set([start])

        counter = 0

        while queue:
            l = len(queue)
            added = False

            for _ in range(l):
                curr = queue.popleft()

                for c in graph[curr]:
                    if c not in visited:
                        added = True
                        visited.add(c)
                        queue.append(c)

            if added:
                counter += 1

        return counter