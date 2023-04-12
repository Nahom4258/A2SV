class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def helper(vertex, arr):
            if vertex == len(graph) - 1:
                ans.append(arr[::] + [vertex])
                return

            for neighbour in graph[vertex]:
                helper(neighbour, arr+[vertex])

            return

        helper(0, [])

        return ans