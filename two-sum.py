class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        index = dict() # (index, number)
        for i in range(n):
            index[nums[i]] = i

        for i in range(n):
            if (target-nums[i]) in index and index[(target-nums[i])] != i:
                return [i, index[(target-nums[i])]]

        return [0, 0]

        # time - O(n)
        # space - O(n)