# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])

        while queue:
            parent = queue.popleft()

            if parent.left:
                graph[parent.val].append(parent.left.val)
                graph[parent.left.val].append(parent.val)
                queue.append(parent.left)
            if parent.right:
                graph[parent.val].append(parent.right.val)
                graph[parent.right.val].append(parent.val)
                queue.append(parent.right)

        # print('ans: ', graph)
        visited = set()
        ans = []
        def dfs(head, counter):
            if counter == k:
                nonlocal ans
                ans.append(head)

            visited.add(head)

            for neighbour in graph[head]:
                if neighbour not in visited:
                    dfs(neighbour, counter+1)

            return

        dfs(target.val, 0)

        return ans