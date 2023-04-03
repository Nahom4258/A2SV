class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # using cyclic sort
        ans = []

        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                continue
                
            i += 1

        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])
                ans.append(i+1)

        return ans