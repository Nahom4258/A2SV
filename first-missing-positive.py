class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                continue

            i += 1

        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1

        return len(nums) + 1