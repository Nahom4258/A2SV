class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        maxim = 0
        def backtrack(temp, index, start):
            nonlocal maxim
            counter[index] += 1

            maxim = max(maxim, index)
            
            if temp == len(nums):
                return
            for i in range(start, len(nums)):
                last = index
                index |= nums[i]
                backtrack(temp+1, index, i+1)
                index = last

        backtrack(0, 0, 0)
        return counter[maxim]