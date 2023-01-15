class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        unique = 0
        rows_to_zero = set()
        cols_to_zero = set()
        for i in range(len(matrix) * len(matrix[0])):
            row = unique // len(matrix[0])
            col = unique % len(matrix[0])
            
            if matrix[row][col] == 0:
                rows_to_zero.add(row)
                cols_to_zero.add(col)
                
            unique += 1
            
        unique = 0
        for i in range(len(matrix) * len(matrix[0])):
            row = unique // len(matrix[0])
            col = unique % len(matrix[0])
            
            if row in rows_to_zero or col in cols_to_zero:
                matrix[row][col] = 0
                
            unique += 1
            
            