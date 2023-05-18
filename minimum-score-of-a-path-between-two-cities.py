class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        union_graph = {i: i for i in range(1, n+1)}
        score = defaultdict(lambda: float('inf'))
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

        for a, b, s in roads:
            score[a] = min(score[a], s)
            score[b] = min(score[b], s)
            union(a, b)

        minim = float('inf')
        for node in range(1, n+1):
            if find(1) == find(node):
                minim = min(minim, score[node])

        return minim