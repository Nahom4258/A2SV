class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = dict()
        size = dict()
        union_graph = dict()
        p_names = []

        for idx, acc in enumerate(accounts):
            for i in range(1, len(acc)):
                union_graph[acc[i]] = acc[i]
                size[acc[i]] = 1  
                parents[acc[i]] = idx
            p_names.append(acc[0])

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
                
        for acc in accounts:
            for i in range(2, len(acc)):
                union(acc[1], acc[i])

        ans = defaultdict(list)
        for key in union_graph:
            ans[parents[find(union_graph[key])]].append(key)
        
        ret = []
        for key in ans:
            temp = []
            temp.append(p_names[key])
            temp.extend(sorted(ans[key]))
            ret.append(temp)
            
        return ret