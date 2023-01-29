class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        left_ptr = 0
        right_ptr = len(nums) - 1
        
        nums.sort()
        
        operations = 0
        while left_ptr < right_ptr:
            if nums[left_ptr] + nums[right_ptr] > k:
                right_ptr -= 1
            elif nums[left_ptr] + nums[right_ptr] < k:
                left_ptr += 1
            else:
                operations += 1
                left_ptr += 1
                right_ptr -= 1
                
        return operations