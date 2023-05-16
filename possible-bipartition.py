class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dislike in dislikes:
            a, b = dislike
            graph[a].append(b)
            graph[b].append(a)

        nodes = [-1] * (n + 1)

        # DFS function to color the graph
        def dfs(person, color):
            nodes[person] = color
            for neighbor in graph[person]:
                if nodes[neighbor] == color:
                    return False
                if nodes[neighbor] == -1 and not dfs(neighbor, 1 - color):
                    return False
            return True

        # Color each person and check if it is possible
        for i in range(1, n + 1):
            if nodes[i] == -1 and not dfs(i, 0):
                return False

        return True