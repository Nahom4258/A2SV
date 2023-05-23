class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        if n <= 0:
            return []
        if n == 1:
            return [0]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            indegree[a] += 1
            indegree[b] += 1

        queue = deque()

        for key in indegree:
            if indegree[key] == 1:
                queue.append(key)
                
        while n > 2:
            length = len(queue)
            n -= length

            for _ in range(length):
                curr = queue.popleft()

                for child in graph[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        queue.append(child)

        return set(queue)