class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_arr = []
        
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
                    
            count_arr.append(counter)
            
        return count_arr