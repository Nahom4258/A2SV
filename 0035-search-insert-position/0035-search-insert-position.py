class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pointer = 0
        ans = -1
        while pointer < len(nums):
            if nums[pointer] >= target:
                ans = pointer
                break
            pointer += 1

        # edge case where the insert position is to append on the array
        if ans == -1:
            ans = len(nums)
        return ans