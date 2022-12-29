class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = 1
        counter = 0
        
        while right_pointer < len(nums):
            if nums[left_pointer] == nums[right_pointer]:
                counter += 1
                right_pointer += 1
                
                if right_pointer >= len(nums):
                    left_pointer += 1
                    right_pointer = left_pointer + 1
                continue
                
            right_pointer += 1
            if right_pointer >= len(nums):
                left_pointer += 1
                right_pointer = left_pointer + 1
            
        return counter