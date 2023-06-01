class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for i in range(n)] for j in range(m)]
        memo[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # check up
                if 0 <= i-1 < m:
                    memo[i-1][j] += memo[i][j]

                # check left
                if 0 <= j-1 < n:
                    memo[i][j-1] += memo[i][j]

        # print('me: ', memo)

        return memo[0][0]