class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
            for this we'll obviously use binary search, but the main thing we
            need to worry about is, how are we going to refer to the numbers to make it binary search.
            The solution is to assign each grid numbers 1 to mxn. Then use the number to convert to row/col
            to check the values and do the binary searc.

            tldr;  assume the matrix is a flat list and do binary search on it :)
        '''

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows*cols) - 1

        while l <= r:
            mid = (l+r) // 2
            row, col = mid//cols, mid%cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False