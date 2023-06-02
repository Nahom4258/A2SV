class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = 0
        
        def dfs(curr, counter, degree: dict):
            if curr >= len(requests):
                # check the complete requests
                if list(degree.values()).count(0) == len(degree):
                    nonlocal max_requests
                    max_requests = max(max_requests, counter)
                return

            fr, to = requests[curr]

            degree[fr] += 1
            degree[to] -= 1

            dfs(curr+1, counter+1, degree)

            degree[fr] -= 1
            degree[to] += 1

            dfs(curr+1, counter, degree)

            return

        dfs(0, 0, {i: 0 for i in range(n)})

        return max_requests