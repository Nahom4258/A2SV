class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)

        for rich in richer:
            a, b = rich

            graph[b].append(a)

        ans = [None] * len(quiet)

        # print('ans; ', graph)

        def dfs(node):
            nonlocal ans
            temp = node

            for n in graph[node]:
                if not ans[n]:
                    dfs(n)
                temp = min(temp, ans[n], key=lambda x: quiet[x])

            ans[node] = temp

            return

        for i in range(len(quiet)):
            if not ans[i]:
                dfs(i)

        return ans