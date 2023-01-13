class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix[0]) * len(matrix)):
            if matrix[row // len(matrix[0])][row % len(matrix[0])] == target:
                return True
            
        return False