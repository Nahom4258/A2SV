class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n

        for i in range(n-1, -1, -1):
            st = i+1
            for j in range(st, n):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], memo[j]+1)

        return max(memo)