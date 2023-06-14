class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = dict()

        def dp(index, sum):
            if sum == 0:
                return 1
            if sum < 0:
                return 0

            if sum not in memo:
                temp_sum = 0
                for i in range(len(nums)):
                    temp_sum += dp(i, sum-nums[i])

                memo[sum] = temp_sum

            return memo[sum]

        return dp(0, target)