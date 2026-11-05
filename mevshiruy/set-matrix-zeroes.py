class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        the main question here is how do we make sure that we aren't confusing original zero and changed zero, we can store original zero grid in hash map for fast lookup, iterate, change row, col
        '''

        row, col = len(matrix), len(matrix[0])
        zeros = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeros.add((i, j))

        print('zer:', zeros)

        def change_to_zeros(t_i, t_j):
            # whole column
            for i in range(row):
                matrix[i][t_j] = 0

            # whole row
            for j in range(col):
                matrix[t_i][j] = 0

        for i in range(row):
            for j in range(col):
                if (i, j) in zeros:
                    change_to_zeros(i, j)