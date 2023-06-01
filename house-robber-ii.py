class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = dict()

        def dp(n, sum, start):
            if n >= len(nums)-1 and start:
                return 0
            if n >= len(nums) and not start:
                return 0

            if n+1 not in memo:
                memo[n+1] = dp(n+1, sum+nums[n], start)

            if n+2 not in memo:
                memo[n+2] = dp(n+2, sum+nums[n], start)

            return max(nums[n] + memo[n+2], memo[n+1])

        # print('0: ', dp(0, 0))
        # print('mem: ', memo)
        first = dp(0, 0, True)
        memo = dict()
        sec = dp(1, 0, False)

        return max(first, sec)