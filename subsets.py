class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(arr, current):
            if current > len(nums) - 1:
                ans.append(arr)
                return

            helper(arr, current + 1)
            helper(arr + [nums[current]], current + 1)

        helper([], 0)

        return ans