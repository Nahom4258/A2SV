class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def validate_board(num, row, col):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:
                    return False

            row_start = (row//3) * 3
            col_start = (col//3) * 3

            for r in range(row_start, row_start+3):
                for c in range(col_start, col_start+3):
                    if board[r][c] == num:
                        return False

            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in range(1, 10):
                        if validate_board(str(num), row, col):
                            board[row][col] = str(num)
                            if self.solveSudoku(board):
                                return True
                            board[row][col] = '.'

                    return False

        return True