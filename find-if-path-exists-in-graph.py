class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union_graph = {i: i for i in range(n)}
        size = [1] * n

        def find(a):
            if union_graph[a] != a:
                union_graph[a]=find(union_graph[a])

            return union_graph[a]

        def union(a, b):
            r_a, r_b = find(a), find(b)

            if r_a != r_b:
                if size[r_a] < size[r_b]:
                    union_graph[r_a] = r_b
                    size[r_b] += size[r_a]
                else:
                    union_graph[r_b] = r_a
                    size[r_a] += size[r_b]

        for a, b in edges:
            union(a, b)
        # print('un: ', union_graph)

        return find(source) == find(destination)