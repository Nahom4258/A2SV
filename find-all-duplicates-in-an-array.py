class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()

        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[i] == nums[j] and i != j:
                ans.add(nums[i])
                i += 1
            else:
                i += 1
                
        return ans