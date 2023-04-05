class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for pos in range(32):
            count = 0

            for num in nums:
                count += (num + 2 ** 31) & (1 << pos)

            if count % 3:
                ans += 2 ** pos

        return ans - (2 ** 31)