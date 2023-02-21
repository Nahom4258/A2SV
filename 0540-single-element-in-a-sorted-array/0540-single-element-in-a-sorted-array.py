class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        while start <= end:
            if nums[start] == nums[start + 1]:
                start = start + 2
            else:
                return nums[start]
            
            if nums[end] == nums[end - 1]:
                end = end - 2
            else:
                return nums[end]