class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []

        for num in nums:
            if num not in unique:
                unique.append(num)

        for index, num in enumerate(unique):
            nums[index] = num

        return len(unique)