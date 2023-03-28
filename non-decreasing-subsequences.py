class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def helper(index, arr):
            if index >= len(nums):
                if len(arr) >= 2:
                    ans.add(tuple(arr))
                return

            print("here: ", arr)
            # arr.append(nums[index])
            # if len(arr) >= 2:
            #     if arr[len(arr)-2] <= arr[-1]:
            #         ans.add(tuple(arr))
            # arr.pop()
            if not arr or nums[index] >= arr[-1]:
                helper(index+1, arr+[nums[index]])

            helper(index+1, arr)
            
            return

        # for i in range(len(nums)):
        helper(0, [])

        print('ans: ', ans)

        return ans