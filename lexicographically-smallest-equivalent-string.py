class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union_graph = {i: i for i in list(string.ascii_lowercase)}

        def find(a):
            if union_graph[a] != a:
                union_graph[a] = find(union_graph[a])

            return union_graph[a]

        def union(a, b):
            rep_a, rep_b = find(a), find(b)

            if rep_a < rep_b:
                union_graph[rep_b] = rep_a
            else:
                union_graph[rep_a] = rep_b

        for i in range(len(s1)):
            a, b = s1[i], s2[i]
            if find(a) != find(b):
                union(a, b)

        ans = list(baseStr)
        for i in range(len(ans)):
            ans[i] = find(ans[i])

        return ''.join(ans)