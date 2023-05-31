class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        ans = [0] * (n+1)
        memo = dict()
        
        def dp(val):
            if val == 0 or val == 1:
                return val

            if val not in memo:
                if val % 2 == 0:
                    memo[val] = dp(val//2)
                    ans[val] = memo[val]
                else:
                    memo[val] = dp((val)//2) + dp(((val)//2)+1)
                    ans[val] = memo[val]

            return memo[val]

        ans[n] =  dp(n)

        for i in range(n, -1, -1):
            if i % 2 != 0:
                ans[i] = dp(i)

        return max(ans)