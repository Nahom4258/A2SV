class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row_n = m
        col_n = n
        
        memo = [[0 for x in range(col_n)] for _ in range(row_n)]
        memo[row_n-1][col_n-1] = 1

        for row in range(row_n-1, -1, -1):
            for col in range(col_n-1, -1, -1):
                right, down = 0, 0
                if row+1 < row_n:
                    down = memo[row+1][col]
                if col+1 < col_n:
                    right = memo[row][col+1]

                memo[row][col] += (right + down)

        return memo[0][0]