class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        copy = nums[:]
        for num in nums:
            copy.append(int(str(num)[::-1]))
            
        return len(set(copy))