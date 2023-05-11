class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestor = defaultdict(set)
        indegree = defaultdict(int)

        for edge in edges:
            a, b = edge
            graph[a].append(b)
            indegree[b] += 1


        queue = deque()
        for i in range(n):
            if not indegree[i]:
                queue.append(i)

        while queue:
            curr = queue.popleft()

            for child in graph[curr]:
                ancestor[child].add(curr)
                ancestor[child] = ancestor[child].union(ancestor[curr])

                indegree[child] -= 1

                if not indegree[child]:
                    queue.append(child)

        ans = []
        for i in range(n):
            temp = ancestor[i]
            ans.append(sorted(temp))

        return ans