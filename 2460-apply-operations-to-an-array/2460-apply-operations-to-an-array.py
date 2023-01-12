class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = 0
        
        # edge case when last number is diff. from 0
        
        while right_pointer < len(nums):
            if right_pointer < len(nums) - 1 and nums[right_pointer] == nums[right_pointer + 1]:
                nums[right_pointer] *= 2
                nums[right_pointer + 1] = 0
                
            if nums[right_pointer] != 0:
                nums[right_pointer], nums[left_pointer] = nums[left_pointer], nums[right_pointer]
                left_pointer += 1
                
            right_pointer += 1
            
        return nums