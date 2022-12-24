class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        left_pointer = 0
        right_pointer = len(nums) - 1
        
        # iterate through nums
        for i in range(len(nums)):
            # if nums[i] equals val, change to '_'
            if nums[i] == val:
                nums[i] = '_'
                k -= 1
        
        # iterate through nums
        while right_pointer > left_pointer:
            # change pointers if condition isn't met
            if nums[left_pointer] != '_':
                left_pointer += 1
                continue
            if nums[right_pointer] == '_':
                right_pointer -= 1
                continue
            
            # swap if left_pointer is '_' & right_pointer is number
            if nums[left_pointer] == '_' and nums[right_pointer] != '_':
                # swap '_' with num value
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
                right_pointer -= 1
            
        print(k)
        return k