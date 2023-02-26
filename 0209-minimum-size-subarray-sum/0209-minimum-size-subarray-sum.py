class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minim = 1000000001
        add = 0
        
        left_ptr = 0
        right_ptr = 0
        while right_ptr < len(nums):
            add += nums[right_ptr]
            right_ptr += 1
            
            while left_ptr < right_ptr and add >= target:
                add -= nums[left_ptr]
                left_ptr += 1
                
                minim = min(minim, right_ptr - left_ptr + 1)
                    
        return 0 if minim == 1000000001 else minim