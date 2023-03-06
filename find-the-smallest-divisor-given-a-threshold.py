class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        ans = end

        while start <= end:
            mid = start + (end - start) // 2
            res = self.divisor_sum(nums, mid)
            if res <= threshold:
                ans = min(ans, mid)
                end = mid - 1
            elif res > threshold:
                start = mid + 1

        return ans


    def divisor_sum(self, nums, divisor):
        add = 0
        for i in range(len(nums)):
            add += ceil(nums[i]/divisor)

        return add