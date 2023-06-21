class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        def dp(num, operations, prev):
            if num == n:
                return operations

            if num > n:
                return 0

            left = dp(num+prev, operations+1, prev)
            right = dp(num+num, operations+2, num)

            if left != 0 and right != 0:
                return min(left, right)
            elif left == 0 and right != 0:
                return right
            elif right == 0 and left != 0:
                return left
            else:
                return 0

        return dp(2, 0, 1) + 2