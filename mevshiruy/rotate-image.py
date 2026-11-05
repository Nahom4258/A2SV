class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # not optimal solution ;)

        # copy org matrix, because we'll do in place
        rows, cols = len(matrix), len(matrix[0])
        copy_mat = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                copy_mat[i][j] = matrix[i][j]
                
        # iterate copy matrix row-- and col++
        for i in range(rows-1, -1, -1):
            for j in range(cols):
                matrix[j][rows-i-1] = copy_mat[i][j]