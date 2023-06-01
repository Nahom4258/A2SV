class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()

        def dp(n, sum):
            if n >= len(nums):
                return 0

            if n+1 not in memo:
                memo[n+1] = dp(n+1, sum+nums[n])

            if n+2 not in memo:
                memo[n+2] = dp(n+2, sum+nums[n])

            return max(nums[n] + memo[n+2], memo[n+1])

        # print('0: ', dp(0, 0))
        # print('mem: ', memo)

        return max(dp(0, 0), dp(1, 0))