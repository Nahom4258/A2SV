class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # define pointers
        pointer = 0
        # sort the list
        nums.sort()
        
        while pointer < len(nums):
            if nums[pointer] != pointer: 
                return pointer
            
            pointer += 1
            
        return len(nums)