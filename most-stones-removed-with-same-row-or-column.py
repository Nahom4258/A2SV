class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        union_graph = {i: i for i in range(len(stones))}
        size = {i: 1 for i in range(len(stones))}

        def find(a):
            if union_graph[a] != a:
                union_graph[a] = find(union_graph[a])

            return union_graph[a]

        def union(a, b):
            rep_a, rep_b = find(a), find(b)

            if rep_a != rep_b:
                if size[rep_a] < size[rep_b]:
                    union_graph[rep_a] = rep_b
                    size[rep_b] += size[rep_a]
                else:
                    union_graph[rep_b] = rep_a
                    size[rep_a] += size[rep_b]

        for i in range(len(stones)):
            for j in range(i, len(stones)):
                x, y = stones[i], stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    union(i, j)

        ans = defaultdict(int)
        for i in range(len(stones)):
            ans[find(i)] += 1

        ret = 0
        for key in ans:
            ret += ans[key] - 1

        return ret