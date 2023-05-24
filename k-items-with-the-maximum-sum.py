class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [numOnes, numZeros, numNegOnes]
        n = [1, 0, -1]

        maxim = 0
        for i in range(len(nums)):
            while nums[i] > 0 and k > 0:
                maxim += n[i]
                nums[i] -= 1
                k -= 1

            if k <= 0:
                break

        return maxim