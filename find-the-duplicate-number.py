class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i]-1 < len(nums) and nums[i] != nums[nums[i]-1] and i != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                continue
            i += 1

        print('ans: ', nums)
        for i in range(len(nums)):
            if i+1 != nums[i] and nums[i] == nums[nums[i]-1]:
                return nums[i]

        return len(nums)