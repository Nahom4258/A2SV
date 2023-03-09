class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()

        def helper(arr):
            if len(arr) == len(nums):
                ans.append(arr[::])
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    helper(arr+[num])
                    visited.remove(num)

        helper([])

        return ans