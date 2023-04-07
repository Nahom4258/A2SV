class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        def dfs(current):
            if current == destination:
                return True

            visited.add(current)
            for neighbour in graph[current]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True

            return False

        return dfs(source)