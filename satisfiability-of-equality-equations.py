class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_graph = {i: i for i in list(string.ascii_lowercase)}
        size = {i: 1 for i in list(string.ascii_lowercase)}

        def find(a):
            if union_graph[a] != a:
                union_graph[a] = find(union_graph[a])

            return union_graph[a]

        def union(a, b):
            rep_a, rep_b = find(a), find(b)

            if size[rep_a] < size[rep_b]:
                union_graph[rep_a] = rep_b
                size[rep_b] += size[rep_a]
            else:
                union_graph[rep_b] = rep_a
                size[rep_a] += size[rep_b]

        for eqn in equations:
            x, t1, t2, y = list(eqn)
            if t1 == '=' and t2 =='=':
                union(x, y)

        for eqn in equations:
            x, t1, t2, y = list(eqn)
            if (t1 == '=' and find(x) != find(y)) or (t1 == '!' and find(x) == find(y)):
                return False

        # print('union: ', union_graph)

        return True