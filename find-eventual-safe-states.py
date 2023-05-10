class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = graph
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(g)):
            for child in g[i]:
                graph[child].append(i)
                indegree[i] += 1

        queue = deque()

        for i in range(len(g)):
            if not indegree[i]:
                queue.append(i)

        ans = []

        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for child in graph[curr]:
                indegree[child] -= 1

                if not indegree[child]:
                    queue.append(child)

        return sorted(ans)