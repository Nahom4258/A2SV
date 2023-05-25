class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        union_graph = [i for i in range(n)]
        size = [i for i in range(n)]

        def find(a):
            if union_graph[a] != a:
                union_graph[a] = find(union_graph[a])

            return union_graph[a]

        def union(a, b):
            rep_a, rep_b = find(a), find(b)

            if size[rep_a] < size[rep_b]:
                union_graph[rep_a] = rep_b
                size[rep_b] -= size[rep_a]
            else:
                union_graph[rep_b] = rep_a
                size[rep_a] -= size[rep_b]

        for a, b in pairs:
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        for key in groups:
            groups[key].sort(key=lambda x: s[x], reverse=True)

        ans = [''] * n
        for i in range(n):
            ans[i] = s[groups[find(i)].pop()]

        return ''.join(ans)