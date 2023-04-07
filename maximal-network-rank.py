class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        maxim = 0

        for i in range(len(roads)):
            graph[roads[i][0]].add(roads[i][1])
            graph[roads[i][1]].add(roads[i][0])

        for i in range(n):
            for j in range(n):
                if i != j:
                    temp = list(graph[i]) + list(graph[j])
                    maxim = max(maxim, len(temp) - (1 if i in graph[j] else 0))

        return maxim