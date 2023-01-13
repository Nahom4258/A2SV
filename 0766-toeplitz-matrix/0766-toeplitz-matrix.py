class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for unique in range(len(matrix[0]) * len(matrix)):
            row = unique // len(matrix[0])
            col = unique % len(matrix[0])
            value = matrix[row][col]
            while row < len(matrix) and col < len(matrix[0]):
                if value != matrix[row][col]:
                    return False
                row += 1
                col += 1
            
        return True