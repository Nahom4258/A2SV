class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [x for x in range(1, n + 1)]
        
        pointer = 0
        counter = 1
        remove_counter = 0
        while remove_counter < n - 1 :
            if counter == k and nums[pointer % n] != 0:
                nums[pointer % n] = 0
                counter = 1
                remove_counter += 1
                
            if nums[pointer % n] != 0:
                counter += 1
                  
                
            pointer += 1
            
        nums = set(nums)
        
        for val in nums:
            if val != 0:
                return val
            
            
        
        