class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        i = 0
        for j in range(cols):
            new_r, new_c = i + 1, j + 1

            while new_r < rows and new_c < cols:
                if matrix[new_r][new_c] != matrix[new_r-1][new_c-1]:
                    return False

                new_r += 1
                new_c += 1

        j = 0
        for i in range(1, rows):
            new_r, new_c = i + 1, j + 1

            while new_r < rows and new_c < cols:
                if matrix[new_r][new_c] != matrix[new_r-1][new_c-1]:
                    return False

                new_r += 1
                new_c += 1

        return True
