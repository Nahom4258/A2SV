class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        add = sum(nums[:k])
        max_sum = add
        
        for i in range(k, len(nums)):
            add += nums[i]
            add -= nums[i - k]
            max_sum = max(max_sum, add)
            
        return max_sum/k