class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)

        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

        ans = [0] * n

        def dfs(node, parent):
            count = Counter()

            for n in graph[node]:
                if n != parent:
                    count += dfs(n, node)

            count[labels[node]] += 1
            ans[node] = count[labels[node]]

            return count

        dfs(0, -1)

        return ans