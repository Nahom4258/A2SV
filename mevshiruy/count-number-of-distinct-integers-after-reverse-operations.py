class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        # not optimal solution (pretty lazy solution) ;)

        n = len(nums)
        unique = set(nums[::])

        for num in nums:
            unique.add(int(str(num)[::-1]))

        return len(unique)