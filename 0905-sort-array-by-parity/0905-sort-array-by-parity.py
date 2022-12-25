class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # define necessary pointers
        left_pointer = 0
        right_pointer = 1
        
        # iterate through the list
        while right_pointer < len(nums):
            # left_pointer always checks for an odd number
            if nums[left_pointer] % 2 == 0:
                left_pointer += 1
                right_pointer += 1
                continue
                
            if nums[right_pointer] % 2 != 0:
                right_pointer += 1
                continue
                
            # if left_ptr is pointing at odd & right_ptr is pointing at even, SWAP & increment pointers
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer += 1
            
        return nums