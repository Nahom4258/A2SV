class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        i = 0
        while i < len(nums):
            if nums[i]-1 < len(nums) and nums[i] != nums[nums[i]-1] and i+1 != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                continue

            i += 1

        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(i+1)

        return ans