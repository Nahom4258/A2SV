class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # using unique number for each cell
        # row_index = unique_no // no_of_cols
        # col_index = uniquie_no % no_of_cols
        
        for unique in range(len(matrix[0]) * len(matrix)):
            if matrix[unique // len(matrix[0])][unique % len(matrix[0])] == target:
                return True
            
        return False