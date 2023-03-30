# using bit-manipulation to hold the visited values
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def checkKth(num, k):
            return num & (1 << k) != 0

        def toggleKth(num, k):
            num = num ^ (1 << k)
            
            return num

        ans = []
        visited = 0

        def helper(arr):
            if len(arr) == len(nums):
                ans.append(arr[::])
                return

            for i in range(len(nums)):
                nonlocal visited
                if not checkKth(visited, i):
                    visited = toggleKth(visited, i)
                    helper(arr+[nums[i]])
                    visited = toggleKth(visited, i)

        helper([])

        return ans