class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dfs(sum):
            if sum == 0:
                return 0

            if sum not in memo:
                memo[sum] = float('inf')
                for i in range(len(coins)-1, -1, -1):
                    if sum-coins[i] >= 0:
                        memo[sum] = min(memo[sum], dfs(sum-coins[i]))

            return memo[sum]+1

        ans = dfs(amount)

        return -1 if ans == float('inf') else ans