class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        memo = dict()

        def dp(idx, add):
            if idx >= n:
                return add if add >= 0 else inf

            key = (idx, add)
            if key in memo:
                return memo[key]

            memo[key] = min(dp(idx+1, add-stones[idx]), dp(idx+1, add+stones[idx]))

            return memo[key]

        return dp(0, 0)