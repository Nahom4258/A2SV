class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = -1
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                ans = middle + 1
                start = middle + 1
            else:
                ans = middle
                end = middle - 1
            
        return ans