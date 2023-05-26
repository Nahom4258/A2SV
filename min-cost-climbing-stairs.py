class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()

        def dp(n, sum):
            if n >= len(cost):
                return 0

            a, b = 0, 0
            if n+1 not in memo:
                a = dp(n+1, sum+cost[n])
                memo[n+1] = a
            else:
                a = memo[n+1]

            if n+2 not in memo:
                b = dp(n+2, sum+cost[n])
                memo[n+2] = b
            else:
                b = memo[n+2]

            sum = cost[n] + min(a, b)

            return sum

        return min(dp(0, 0), dp(1, 0))