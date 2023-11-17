class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        if n == 1:
            return mat[0][0]

        sum = 0
        for i in range(n):
            sum += mat[i][i]

        for i in range(n-1, -1, -1):
            sum += mat[n-i-1][i]

        if n % 2 != 0:
            return sum-mat[n//2][n//2]

        return sum