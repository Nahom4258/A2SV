class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort
        freq_arr = [0, 0, 0]
        
        for num in nums:
            freq_arr[num] += 1
            
        curr = 0
        index = 0
        while curr < len(nums):
            for i in range(freq_arr[index]):
                nums[curr] = index
                curr += 1
            index += 1
        