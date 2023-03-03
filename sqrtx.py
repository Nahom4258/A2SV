class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        ans = 0

        while start <= end:
            mid = (start + end) // 2
            if mid * mid < x:
                ans = max(ans, mid)
                start = mid + 1
            elif mid * mid > x:
                end = mid - 1
            else:
                return mid

        return ans