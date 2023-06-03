class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()

        def dp(row, col):
            if row == 1 and col == 1:
                return 1

            if row <= 0 or col <= 0:
                return 0

            if (row, col) not in memo:
                down = dp(row-1, col)
                right = dp(row, col-1)
                memo[(row, col)] = down + right

            return memo[(row, col)]

        return dp(m, n)