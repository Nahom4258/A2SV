class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(index, sum):
            if index >= len(nums):
                return target == sum

            if (index, sum) not in memo:
                memo[(index, sum)] = dp(index+1, sum+nums[index]) + dp(index+1, sum-nums[index])

            return memo[(index, sum)]

        return dp(0, 0)