class Solution:
    def minSteps(self, n: int) -> int:
        memo = dict()
        
        if n == 1:
            return 0

        def dp(op, curr, clipboard):
            if curr > n:
                return inf

            if curr == n:
                return 0

            key = (curr, clipboard)
            if key in memo:
                return memo[key]

            if op == 'p':
                copy = dp('c', curr, curr)
                paste = dp('p', curr+clipboard, clipboard)
                memo[key] = min(copy, paste) + 1
            else:
                memo[key] = dp('p', curr+clipboard, clipboard) + 1

            return memo[key]

        return dp('c', 1, 1) + 1