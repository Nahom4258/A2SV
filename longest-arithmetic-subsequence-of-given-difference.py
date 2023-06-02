class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = dict()
        maxim = 1

        for i in range(len(arr)-1, -1, -1):
            curr = arr[i] + difference
            if curr in memo:
                memo[arr[i]] = memo[curr] + 1
                maxim = max(memo[arr[i]], maxim)
            else:
                memo[arr[i]] = 1

        return maxim