class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # define left & right pointers for the sliding window: these pointers encompase the sides of the riangle
        left_pointer = 0
        right_pointer = 2
        perimeter = 0
        
        # sort the given list of triangle sizes
        nums.sort()
        
        # use while loop for sliding window
        while right_pointer < len(nums):
            # test if its a triangle using triangle inequalities theorem
            if (nums[left_pointer] + nums[left_pointer + 1] > nums[right_pointer] and
                nums[left_pointer] + nums[right_pointer] > nums[left_pointer + 1] and
                nums[left_pointer + 1] + nums[right_pointer] > nums[left_pointer]):
                    # set perimeter the maximum of current or the previous
                    perimeter = max(perimeter, nums[left_pointer] + nums[left_pointer + 1] + nums[right_pointer])
            
            # increment left & right pointer no matter what
            left_pointer += 1
            right_pointer += 1
                    
        return perimeter