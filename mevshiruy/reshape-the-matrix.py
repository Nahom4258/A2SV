class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n_r, n_c = len(mat), len(mat[0])

        if n_r * n_c != r * c:
            return mat

        # create the new matrix
        new_mat = [[0] * c for _ in range(r)]

        # linearly copy values
        values = []
        for i in range(n_r):
            for j in range(n_c):
                values.append(mat[i][j])

        # fill new matrix
        for i in range(len(values)):
            row, col = i//c, i%c
            new_mat[row][col] = values[i]

        return new_mat