class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxim = max(nums)
        minim = min(nums)

        min_l, min_r = minim-k, minim+k
        max_l, max_r = maxim-k, maxim+k

        if min_r >= max_l:
            return 0

        return abs(min_r-max_l)