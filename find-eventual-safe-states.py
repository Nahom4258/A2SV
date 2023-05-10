class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 0 - not processed 1 - being processes 2 - already processed
        g = graph
        graph = defaultdict(list)

        for i in range(len(g)):
            for child in g[i]:
                graph[i].append(child)

        # print('ans; ', graph)
        color = [0] * len(g)
        def dfs(node):
            color[node] = 1
            
            found = True
            for neighbour in graph[node]:
                if color[neighbour] == 1:
                    return False
                if color[neighbour] == 0:
                    found = found and dfs(neighbour)

            if found:
                color[node] = 2

            return found

        for i in range(len(g)):
            if color[i] == 0:
                dfs(i)

        # print('ans: ', color)
        ans = []
        for i in range(len(color)):
            if color[i] == 2:
                ans.append(i)

        return ans