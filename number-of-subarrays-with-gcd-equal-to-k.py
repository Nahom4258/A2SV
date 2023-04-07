class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            temp = []
            for j in range(i, len(nums)):
                temp.append(nums[j])
                if gcd(*temp) == k:
                    ans += 1

        return ans