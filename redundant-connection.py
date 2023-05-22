class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union_graph = {i: i for i in range(1, n+1)}
        size = [1] * n

        def find(a):
            if union_graph[a] != a:
                union_graph[a] = find(union_graph[a])

            return union_graph[a]

        def union(a, b):
            rep_a, rep_b = find(a), find(b)

            if size[rep_a-1] < size[rep_b-1]:
                union_graph[rep_a] = rep_b
                size[rep_b-1] += size[rep_a-1]
            else:
                union_graph[rep_b] = rep_a
                size[rep_a-1] += size[rep_b-1]

        def check():
            for i in range(1, n+1):
                if find(1) != find(i):
                    return False

            return True
            
        ans = []
        for a, b in edges:
            if find(a) == find(b):
                ans.append([a, b])
            
            union(a, b)

        return ans[-1]